# Den enkleste innebygde funksjonen i Python
# Starter en ny linje på slutten

print("Hei Verden!")

a = "Hei for andre gang!"
print(a)

a = 5 # Sier hva "a" skal være på nytt (!)
b = 5

print(a+b)
# Må gjøre om til string for å "konkatenere" (legge til)
# Mellomrom kommer ikke automatisk
print("Svaret på a + b er: " + str(a+b))

# Vi har også int() eller float()

# a, b = 1 går ikke
a, b = 1, 2
print(a+b)

# Viktig! Dette lagres som en string, IKKE et tall
# input string = "5" VS input string = 5
input_string = input("Skriv inn et tall: ")
print("Du skrev inn: " + input_string)

# Men dette kommer til å gi en feil
# Feilen er som regel deskriptiv

c = a + input_string

# Ser du helt overordnet og se hva som er galt?
