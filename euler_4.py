def tresiffrede_nummer():
    tall = []
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                tall_string = str(i) + str(j) + str(k)
                tall.append(int(tall_string))

    return tall


tall_liste = tresiffrede_nummer()

palindrom_liste = []

for i in tall_liste:
    for j in tall_liste:
        produkt_string = str(i*j)
        if produkt_string == produkt_string[::-1]:
            palindrom_liste.append(int(produkt_string))

print(sorted(palindrom_liste, reverse=True))