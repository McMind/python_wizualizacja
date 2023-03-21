def wartosc_zakupow(**produkty):
    print(len(produkty))
    wszystko = 0
    for produkt in produkty:
        wszystko += produkty[produkt]
    return wszystko


print(wartosc_zakupow(Sprezone_powietrze=15, Pizza=10, Chipsy=7, Piwo=3))
