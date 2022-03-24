import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

y = []

with open("temperaturer.txt") as fil:
    for linje in fil:
        y.append(int(linje))

x = range(1, len(y)+1)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(integer=True)) # Brukes for å få heltall på x-aksen
ax.plot(x, y)

ax.set(xlabel='Dag', ylabel='Temperatur (C)',
       title='Temperaturer i Gjøvik om sommeren')
ax.grid()

plt.show()
