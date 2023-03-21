from math import sqrt


def pierwiastek(n):
    try:
        wynik = sqrt(n)
    except ValueError:
        print("wpisz liczbę nieujemną")
    else:
        print(wynik)


pierwiastek(4)
pierwiastek(-1)
