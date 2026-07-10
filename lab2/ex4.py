import numpy as np

a = {1: "apple" ,
        3:"banana",
            2: "cherry"}

b = np.argsort(list(a.keys()))
print('index b:',b)
#print('values:',a[b])
print([a[list(a.keys())[i]]for i in b]) #apple cherry banana

print ('*'*50)
c = list(a.keys())
c.sort()
print([a[i]for i in c]) #for i in c -> print(a[i])

for i in c : print(a[i]) #บรรทัดเดียว