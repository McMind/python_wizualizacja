import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('stacjepaliw.xlsx')
df = pd.melt(df,id_vars='Nazwa',var_name='Rok',value_name='zł (mln)')
df_m = df[df['Nazwa'] == 'MAŁOPOLSKIE']
df_s = df[df['Nazwa'] == 'ŚLĄSKIE']

plt.plot(df_m['Rok'],df_m['zł (mln)'], color='darkorange', label='Małopolskie')
plt.plot(df_s['Rok'],df_s['zł (mln)'], color='lime', label='Śląskie')
plt.xlabel('Lata')
plt.ylabel('Zarobki w mln zł')
plt.title('Zarobki na stacjach paliw')
plt.legend(title="Województwa:" ,loc=2)
plt.ylim(600,1300)
plt.savefig('zad3.eps',format='eps')
plt.show()