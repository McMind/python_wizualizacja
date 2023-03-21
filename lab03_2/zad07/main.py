def iloczyn_elementow(* liczby):
    if len(liczby) != 3:
        return -1
    elementy = [liczby[0] * pow(liczby[1],i) for i in range(liczby[2])]
    wynik = 0
    for element in elementy:
        wynik += element
    return wynik

print(iloczyn_elementow(1,4,10))