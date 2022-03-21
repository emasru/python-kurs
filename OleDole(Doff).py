for i in range(1, 100+1):
    output = "" # En tom string

    if i % 3 == 0:
        output += "Ole "
    if i % 5 == 0:
        output += "Dole "
    if output == "":
        output = i

    print(output)
