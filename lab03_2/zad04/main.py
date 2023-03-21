import math


def trojkat_prostokatny(a, b, c):
    przeciwprostokatna = max(a, b, c)
    przyprostokatne = [a, b, c]
    przyprostokatne.remove(przeciwprostokatna)
    if pow(przyprostokatne[0], 2) + pow(przyprostokatne[1], 2) == pow(przeciwprostokatna, 2):
        return True
    return False


a = 3
b = 4
c = 5
print(trojkat_prostokatny(a, b, c))
