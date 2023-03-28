class ciagi():
    def wyswielt_dane(self):
        print(f"a1 = {self.pierwsza_wartosc} , r = {self.roznica}")
        return 0
    def pobierz_elementy(self):
        pass # nie wiem co ta funkcja ma pobierac
    def pobierz_parametry(self,pw,roznica):
        self.pierwsza_wartosc = pw
        self.roznica = roznica
        return 0
    def policz_sume(self,ilosc):
        suma = ((2*self.pierwsza_wartosc+(ilosc-1)*self.roznica)/2)*ilosc
        return suma
    def policz_elementy(self,element):
        n_ty_wyraz = self.pierwsza_wartosc + (element-1)*self.roznica
        return n_ty_wyraz


ciag = ciagi()
ciag.pobierz_parametry(1,-3)
print(f"{ciag.policz_sume(10)}\n{ciag.policz_elementy(25)}")
ciag.wyswielt_dane()