class robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
        return

    def idz_w_gore(self, krok):
        self.y += self.krok * krok
        return 0

    def idz_w_dol(self, krok):
        self.y -= self.krok * krok
        return 0

    def idz_w_lewo(self, krok):
        self.x -= self.krok * krok
        return 0

    def idz_w_prawo(self, krok):
        self.x += self.krok * krok
        return 0

    def pokaz_gdzie_jestes(self):
        print(f"x:{self.x} , y:{self.y}")
        return


robak = robaczek(5, 4, 2)
robak.idz_w_gore(3)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(5)
robak.pokaz_gdzie_jestes()
