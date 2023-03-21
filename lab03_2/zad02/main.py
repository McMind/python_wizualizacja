import random
lista1 = [random.randint(0,100) for i in range(10)]
lista2 = [x for x in lista1 if x % 2 == 0]
print(lista2)