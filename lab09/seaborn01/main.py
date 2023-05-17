import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# sns.set(rc={'figure.figsize': (8, 6)})
# sns.lineplot(x=[i for i in range(1, 5)], y=[i ** 2 for i in range(1, 5)], label='linia nr',
#              color='red', marker='o', linestyle=':')
# sns.lineplot(x=[i for i in range(1, 5)], y=[i ** 2 + 1 for i in range(1, 5)], label='linia nr',
#              color='green', marker='o', linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Wykres liniowy')
# plt.show()

# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# wykres = sns.relplot(kind='line', data=s, label='dane z serii')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=.1, right=.9, bottom=.1, top=.9)
# plt.show()

# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['yellow', 'green', 'red'])
# plt.xlabel('indeksy')
# plt.title('Wykres liniowy danych z Iris dataset')
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# df = pd.DataFrame(data)
#
# plot = sns.relplot(data=df, x='a', y='b', hue='c', palette='bright',
#                    size='d', legend=True)
# plot.set(xticks=data['a'])
# plt.show()

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
plot = sns.barplot(data=df, x='Kontynent', y='Populacja', hue='Kontynent', estimator=np.sum, errorbar=None, dodge=False,
                   palette=['red', 'green', 'blue'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()
