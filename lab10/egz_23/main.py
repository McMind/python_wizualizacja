import matplotlib.pyplot as plt

sizes = [55.5,6.7,13,24.8]
labels = ['Inne','Eska','Radio Zet','RMF FM']
colors = ['purple','green','blue','red']
explode = (0,0,0,0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%2.1f%%', shadow=True, startangle=80, counterclock=False)
plt.title('Wyniki słuchalności - II-IV 2017')

plt.axis('equal')
plt.savefig('zad1.pdf',format='pdf')
plt.show()