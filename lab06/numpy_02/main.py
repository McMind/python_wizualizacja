import numpy as np

#zad1
a = np.arange(0,81,4,)
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

#zad4
def generuj(pod,ile):
    return np.logspace(1,ile,num=ile,base=pod)

print(generuj(4,3))

#zad5
def zad5(dlu):
    tab = np.arange(1,dlu+1)[::-1]
    tab = np.diag(tab,k=2)
    return tab
print(zad5(4))

#zad6
malina = np.array(['malina'])
mrowka = np.array(['mrowka'])
armata = np.array(['armata'])

wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = mrowka
wykreslanka[5::,-1] = armata
#for a in range(6):
 #   wykreslanka[a,a] = malina[0][a]
print(wykreslanka)
#zad7
def macierz_2(n):
    macierz = np.diag([2 for i in range(n)])
    liczba = 4
    for i in range(1,n):
        np.fill_diagonal(macierz[:-i, i:], [liczba for j in range(i)])
        np.fill_diagonal(macierz[i:, :-i], [liczba for j in range(i)])
        liczba += 2
    print(macierz)

macierz_2(5)
