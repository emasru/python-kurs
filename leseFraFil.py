temperaturer = []

with open("temperaturer.txt") as fil:
    for linje in fil:
        temperaturer.append(int(linje))

print(temperaturer)