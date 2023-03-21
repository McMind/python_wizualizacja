def iloczyn_elementow(a=1, b=4, ile=10):
    elementy = [a * pow(b,i) for i in range(ile)]
    wynik = 1
    for element in elementy:
        wynik *= element
    return wynik


print(iloczyn_elementow())
