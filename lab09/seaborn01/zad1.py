import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.subplot(2,2,1)
# sizes_a = [15.7,7.56,12.79,21.51,16.86,25.58]
# labels_a = ["A","F","E","D","C","B"]
# colors_a = ["brown", "blue", "brown", "lime","bisque","magenta"]
# explode_a = (0,0,0,0,0,0.1)
# plt.pie(sizes_a, explode=explode_a, labels=labels_a, colors=colors_a, autopct='%2.2f%%', counterclock=False, startangle=100)
# plt.title("Lewo Góra")
#
# plt.subplot(2,2,4)
# sizes_b = [20.37,16.67,15.74,19.91,9.72,17.59]
# plt.pie(sizes_b, explode=explode_a, labels=labels_a, colors=colors_a, autopct='%2.2f%%', counterclock=False, startangle=110)
# plt.title("Prawo Dół")
# plt.tight_layout()
# #plt.show()

df = pd.read_csv('wynagrodzenia21.csv', delimiter=';', decimal=',')

df = df.melt( id_vars='Województwo', var_name="Rok", value_name='Wartosc')
#m = data[(data['Plec']=="M")].groupby(['Rok'])['Liczba'].sum()
df['Rok'] = df['Rok'].astype(int)
X = 4
df = df[(df['Rok']>=2010)&(df['Rok']<=2013)]
df2 = df[(df["Województwo"]=="LUBUSKIE")]
df3 = df[(df['Województwo']=="WARMIŃSKO-MAZURSKIE")]
plt.bar((df2['Rok']+0.25),df2["Wartosc"], width=0.25, color='r')
plt.bar((df3['Rok']),df3["Wartosc"], width=0.25, color='g')
plt.xticks(ticks=df2['Rok'].astype(int))
plt.yticks(np.arange(0,3300,500))
plt.text(2013.5, 10, 'Filip', verticalalignment='bottom',horizontalalignment='right', fontsize='large')
#print(df3)
plt.savefig('test.jpg',format='jpg')
plt.show()
#print(df)
print(df2)