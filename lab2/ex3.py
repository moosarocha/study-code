import numpy

a = [2,3,9,1,4]

b = numpy.asarray(a) # 23914
#c = numpy.sort(b)
c = numpy.argsort(b) #30142
print (b) 
print (c)
print(b[c])
#a.sort(reverse=True)
#print(a) #9,4,3,2,1