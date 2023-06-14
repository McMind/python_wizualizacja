import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('turystyka1.xlsx',header=[0, 1])
df = pd.melt(df, var_name=['nazwa','rok'], value_name='wartość')
df["nazwa"] = df["nazwa"].str[10:]
df2015 = df[(df['rok'] == '2015')]
df2016 = df[(df['rok'] == '2016')]
plt.plot(df2015['nazwa'],df2015['wartość'], '--r', label="2015")
plt.plot(df2016['nazwa'],df2016['wartość'], ':b', label="2016")
plt.legend(title="rok")
plt.xlabel('kategoria')
plt.ylabel('wartość')
plt.title('Wartości hotelów w poszczególnych latach')
plt.savefig('wykres3.jpg',format='jpg')
plt.show()