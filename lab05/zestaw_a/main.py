import math


def zad1():
    try:
        a = int(input("wpisz a: "))
        b = int(input("wpisz b: "))
        wynik = pow(a, 2) + a * b + pow(b, 2)
        plik = open("zadanie1.txt", "w")
        plik.write(str(wynik))
        plik.close()
    except ValueError:
        print("podaj poprawne liczby")
    except:
        print("inny error")
    else:
        print("wykonano pomyślnie")


def zad2(lista1, lista2):
    wynik = []
    try:
        for i in range(len(lista1)):
            wynik.append(lista1[i] + lista2[i])
    except:
        return "error"
    return wynik


# zad1()
print(zad2([1, 2, 3], [4, 5, 6]))
plik = open("tekst.txt", 'r', encoding="utf-8")
plik.seek(99)
znaki = plik.read(35)
slownik = {}
for znak in znaki:
    if znak.isupper():
        if znak in slownik.keys():
            slownik[znak] += 1
        else:
            slownik[znak] = 1
if (len(slownik.keys())):
    print(slownik)
else:
    print("Słownik jest pusty")
plik.close()

lista3 = [1, 4, 5, 2, 8, 0]
a = 3
lista_wieksza_a = [x for x in lista3 if x > a]
print(lista_wieksza_a)
wynik_wyrazenia = pow(pow(math.e, 3) + pow(math.cos(39), 2), 1 / 5) + pow(2 / 7, 3) + math.pi
wynik_wyrazenia = round(wynik_wyrazenia, 2)
print(wynik_wyrazenia)
