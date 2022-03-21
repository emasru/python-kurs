# Løkker er deler av kode som gjentar seg
# Den enkleste vi har er while-løkken (Så lenge noe er sant)
# Deklarer en variabel som vi bruker til telling
# Disse blir som regel kalt "i" etter tradisjon (muligens indeks)

i = 1

# Indentering er viktig!

while (i < 100):
    print(i)
    i += 1
    # "+=" legger til en verdi


# Hva gjør denne koden?
# Kunne også vært "<=", dette fikser at det går til 100. Hvorfor?
    
# while True:
# Denne er veldig farlig, og bør ikke bli brukt

# All type kode kan være inne i en løkke eller if-setning!
# Men indenteringen gjelder fortsatt

a = 2

if a == 2:
    while (i < 100):
        print(i)
        i += 1
else:
    print("Printer ikke ut tallene")


# Pseudokode


# Kan du skrive et program som printer ut alle partallene fra 0 til 100?
# Pseudokode eller python
