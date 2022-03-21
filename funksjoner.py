# Funksjoner er noe som kan ta input, gjøre noe, og kan returnere en verdi

# En funksjon som printer "Hei verden!"
# En tom parantes betyr at vi ikke tar noe input
def print_verden():
    print("Hei verden!")

print_verden():

# Vi kan også få funksjonen til å returnere det vi skal printe
def print_verden_med_return():
    return "Hei verden!"

print(print_verden_med_return())

# Kan da også lages i en variabel

a = print_verden_med_return()
print(a)

# Parametere brueks for å gi en funksjon litt input
# Tenk typisk matte...

def f(x):
    return x**2

print(f(2))
print(f(4))

# En funksjon kan også kalle på seg selv...
# Dette skal vi se nærmere på men her er et enkelt eksempel

def print_hvis_100(x):
    if x == 100:
        print("Vi har nådd 100") # Legg merke til: trenger ingen else-setning
        return
    print_hvis_100(x+1)


# Python gir en feil hvis du har for mye rekursjon
