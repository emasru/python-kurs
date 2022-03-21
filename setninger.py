# Her bruker vi en if-setning, indentering er viktig her
# Utrykket inni blir "evaluert"

if (4 + 6) == 10:
    print("4 + 6 er jo 10!")


# Modulo operatoren
# Tar resten av to tall

a = 5 % 2
print(a)
b = 4 % 2
print(b)

# Dette gjør den veldig nyttig til bla. partallsjekk

a = 4

# "==" er HELT ulikt "="
# Kan gjøres med og uten parantes
if a % 2 == 0: 
    print(str(a) + " er et partall")

a = 3

# Vi kan la den stå alene, eller...
if a % 2 == 0:
    print(str(a) + " er et partall")
else:
    print(str(a) + " er et oddetall")

'''Eventuelt:
if a % 2 == 0:
    print(str(a) + " er et partall")
elif a % 3 == 0:
    print(str(a) + " er et oddetall")
'''
