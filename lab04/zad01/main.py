liczby = [i*2 for i in range(31)]
print(liczby)
plik = open("liczby.txt","w")
plik.writelines(str(liczby))
plik.close()
