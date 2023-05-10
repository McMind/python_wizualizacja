import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.arange(1,5)
y = x**2

#plt.plot(x,y, 'ro-')
# plt.plot(x,y, 'r-')
# plt.plot(x,y, 'o')
# plt.axis([0,6, 0,20])

a = np.arange(0,5,0.2)
#plt.plot(a,a, 'r-', a, a**2, 'bs', a, a**3, 'g^')
# plt.plot(a,a,'r-', label="liniowa")
# plt.plot(a, a**2, 'bs', label="kwadratowa")
# plt.plot(a, a**3, 'g^', label="sześcienna")
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('wykresy')
# plt.legend(loc="center left")
# plt.savefig('wykres.png')

# b = np.arange(0,10.1,0.1)
# plt.axis([0,10.1, -1,1])
# plt.plot(b,np.sin(b), 'm-.')
# plt.show()

# data = {
#     'a': np.arange(50),
#     'c': np.random.randint(0,50,50),
#     'd': np.random.randn(50)
# }
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('a')
# plt.ylabel('b')
# plt.show()

x1 = np.arange(0,2,0.02)
x2 = np.arange(0,2,0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

# plt.subplot(4,1,1)
# plt.plot(x1,y1)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('wykres sin(x)')
#
# plt.subplot(4,1,4)
# plt.plot(x2,y2, 'r')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = plt.subplots(3,2)
# axs[0,0].plot(x1,y1,'r')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[0,0].set_title('wykres sin(x)')
#
# axs[1,1].plot(x2,y2,'m')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('wykres cos(x)')
#
# axs[2,0].plot(x1,y1,'g')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('sin(x)')
# axs[2,0].set_title('wykres sin(x)')
#
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
#
# plt.show()

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# ts.plot()
# plt.show()

# data = {'Kraj': [
#     'Belgia', 'Indie', 'Brazylia', 'Polska'
# ], 'Stolica': [
#     'Bruksela', "New Delhi", "Brasilia", "Warszawa"
# ], 'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
#     'Populacja': [11109846,1303171035, 207847528, 38675693]
# }
# df = pd.DataFrame(data)
# grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
# # grupa.plot(kind='bar', xlabel='kontynenty', ylabel='Populacja', legend=True, title='Populacja na kontynentach', rot=0)
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('Populacja na kontynentach')
# plt.show()

