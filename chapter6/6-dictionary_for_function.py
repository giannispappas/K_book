eng2sp = {'one':'uno','two':'dos','three':'tres'}
keys_view = eng2sp.keys()
values_view = eng2sp.values()
items_view = eng2sp.items()

for key in keys_view:
    print(key)
    
for value in values_view:
    print(value)
    
for key,value in items_view:
    print key,value
