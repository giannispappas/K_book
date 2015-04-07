#!/usr/bin/env python

import smtpd
import asyncore
import time
import uuid
import pycassa
import re
import sys

class CassSMTPServer(smtpd.SMTPServer):
    def __init__(*args, **kwargs):
        smtpd.SMTPServer.__init__(*args, **kwargs)

    def process_message(self, peer, mailfrom, rcpttos, data):
        now = time.strftime('%a %b %d %T %Y', time.gmtime())
        head = 'From {0} {1}\n'.format(mailfrom, now)
        email = head + data
        user = re.search('(.*)@(.*)', rcpttos[0]).group(1)
        mbox = 'inbox'
        c = pycassa.ConnectionPool('Mail')
        cl = pycassa.cassandra.ttypes.ConsistencyLevel.ONE
        cf = pycassa.ColumnFamily(c, 'Mailboxes', write_consistency_level=cl)
        cf.insert('{0}:{1}'.format(user, mbox),
            {uuid.uuid1() : email})
        cf = pycassa.ColumnFamily(c, 'Users', write_consistency_level=cl)
        cf.insert(user, {mbox : ''})
        return


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8025
    s = CassSMTPServer(('0.0.0.0', port), None)
    asyncore.loop()

# vim:set ts=4 sw=4 et:
