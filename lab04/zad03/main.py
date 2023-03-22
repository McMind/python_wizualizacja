plik = open("tekst2.txt", "w+")
plik.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n")
plik.write("Maecenas nec eros eget felis scelerisque porta.\n")
plik.write("Mauris mollis mi ipsum, sed sodales nisl ultricies aliquam.")
plik.close()
with open("tekst2.txt","r") as plik:
    for linia in plik:
        print(linia,end="")
# plik.seek(0)
# linie = plik.readlines()
# for linia in linie:
#     print(linia, end="")
# plik.close()
