temperaturer = []

with open("temperaturer.txt") as fil:
    for linje in fil:
        temperaturer.append(int(linje))

print(temperaturer)

# Hint: vi kan plotte vanlige lister også
# Hint: len(), range()