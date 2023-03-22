class naZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
        return

    def wyswietl_produkt(self):
        print(f"Nazwa produktu to: {self.nazwa_produktu}\nIlość produktu: {self.ilosc}\n"
            f"Jednostka miary: {self.jednostka_miary}\nCena za jednostkę to: {self.cena_jed}")
        return

    def ile_produktu(self):
        print(f"{self.ilosc} {self.jednostka_miary}")
        return

    def ile_kosztuje(self):
        wartosc = self.ilosc * self.cena_jed
        return wartosc


ziemniaki = naZakupy("ziemniaki", 4, "kg", 3)
ziemniaki.wyswietl_produkt()
ziemniaki.ile_produktu()
print(ziemniaki.ile_kosztuje())
