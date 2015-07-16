inventory = {'apples':430, 'bananas': 312, 'oranges': 525, 'pears':217}
print(inventory)

del inventory['pears']
print(inventory)

inventory['pears']=0
print(inventory)

print(len(inventory))

'apples' in inventory