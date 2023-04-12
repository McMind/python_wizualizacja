import numpy as np

#zad1
a = np.arange(4,84,4)
print(a)

#zad2
b = np.arange(1,2,0.1)
print(b)
c = b.astype('int32')
print(c)

#zad3
def zad3(n):
    tab = np.array([pow(2,x) for x in range(pow(n,2))])
    return tab.reshape(n,n)
print(zad3(5))