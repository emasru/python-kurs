import string

to_dimensjoner = [[2, 3], [4, 5]]

for i in to_dimensjoner:
    for j in i:
        print(j)

alfabet = list(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz'

for i in alfabet:
    for j in alfabet:
        for k in alfabet:
            print(i + j + k)

# Hva kan dette brukes til ?