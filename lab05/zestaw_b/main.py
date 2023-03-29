import math
plik = open("tekst.txt","r",encoding="utf-8")
plik.seek(70)
znaki = plik.read(40)
ilosc_a = znaki.count('a')
if(ilosc_a>0):
    print(f"a występuje: {ilosc_a} razy")
else:
    print("nie ma a w tekscie")
plik.close()

lista_z_liczbami = [3,5,4.5,2,1,0,7.9]
lista_z_liczbami_zmp = [liczba for liczba in lista_z_liczbami if type(liczba) == float]
print(lista_z_liczbami)
print(lista_z_liczbami_zmp)

def zad3(lista):
    pierwsza_liczba = lista[0]
    for liczba in lista:
        pierwsza_liczba += liczba
    lista.append(pierwsza_liczba)
    return lista

print(zad3([4,5,2,1,0,5,3.5]))

wynik_wyrazenia = pow(math.sin(56),2) + pow(pow(4,2)/25+(math.log(85,3)),1/4)
wynik_wyrazenia = round(wynik_wyrazenia,2)
print(wynik_wyrazenia)

def zad5():
    try:
        n = int(input("podaj liczbę n: "))
        if(n<0):
            raise ValueError
        wynik = 0
        for i in range(1,n+1):
            wynik += i
        plik = open("zadanie5.txt","w")
        plik.write(str(wynik))
        plik.close()
    except ValueError:
        print("zła wartość wpisanego argumentu")
    else:
        print("wykonano pomyślnie")

zad5()
