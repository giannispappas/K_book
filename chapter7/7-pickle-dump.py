import pickle
f = open('myfile.txt','wb')
pickle.dump(5.2,f)
pickle.dump([1,2,3],f)
f.close()