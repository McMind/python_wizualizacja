import pandas as pd
import numpy as np

xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx)
#print(df)
print(df[df['Liczba'] > 1000])
print(df[df['Imie'] == "FILIP"])
print(f"Łączna ilość urodzeń: {df['Liczba'].sum()}")
print(f"Liczba urodzeń między 2000-2005 rokiem: {df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005), 'Liczba'].sum()}")
print(f"Liczba urodzeń chłopców: {df.loc[df['Plec'] == 'M' , 'Liczba'].sum()}")
print(f"Liczba urodzeń dziewczynek: {df.loc[df['Plec'] == 'K' , 'Liczba'].sum()}")
