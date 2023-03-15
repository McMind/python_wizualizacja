liczby = []
while len(liczby) != 10:
    liczby.append(int(input("wpisz liczbę ")))
parzyste_liczby = [liczba for liczba in liczby if liczba % 2 == 0]
print(parzyste_liczby)