produkty = {"mleko":"L","cukierki":"g","jajka":"szt","batony":"szt","soki":"L"}
nowa_lista = [produkt for produkt in produkty if produkty[produkt] == "szt"]
print(nowa_lista)