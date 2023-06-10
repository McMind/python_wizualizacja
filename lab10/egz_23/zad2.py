import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('turcja.xlsx',index_col=0)
df = df[df['city'] == 'Ankara']
df = df[df['years'].between(2005,2010)]
df['years'] = df['years'].astype(int)
df['pop'] /= 1e6
X = np.arange(len(df['years']))
plt.bar(df['years'], df['pop'],color='green', width=0.5)
plt.xticks(np.arange(2005,2011),['2005','2006','2007','2008','2009','2010'])
plt.ylim(4,5)
plt.annotate('Strzałka',xy=(2005,df['pop'].iat[0]),xytext=(2005.5, df['pop'].iat[0]+0.2),  arrowprops=dict(facecolor='red'))
plt.xlabel('Rok')
plt.ylabel('Populacja (mln)')
plt.title('Populacja w ciągu lat miasta Ankara')
plt.savefig('zad2.webp',format='webp')
plt.show()