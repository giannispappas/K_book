f=open('C:\Python_book\myfile2.txt','w')
f.write('Numbers:\n')
numbers=[10,12]
f.write(str(numbers[0]))
f.write('--')
f.write(str(numbers[1]))
f.close()
