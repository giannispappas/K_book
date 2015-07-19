def find(string,ch,start=0):
    index = start
    while index < len(string):
        if string[index] == ch:
            return index
        index = index +1
    return -1

print(find('hello','e'))
print(find('hello','e',2))
