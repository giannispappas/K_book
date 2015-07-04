def copyFile(oldFile, newFile):
    f1 = open(oldFile, 'r')
    f2 = open(newFile, 'w')
	
    while True:
        text = f1.read(5)
	if text == ":
        break
	f2.write(text)
	
    f1.close()
    f2.close()
	