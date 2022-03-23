booleansk = True

if booleansk is not True:
    print("Dette printes ikke")
else:
    print("Dette printes")

booleansk = False

if booleansk is not True:
    print("Dette printes")
else:
    print("Dette printes ikke")

if booleansk is False:
    print("Dette printes")
else:
    print("Dette printes ikke")

booleansk = None # Ingenting

if booleansk is not None:
    print("Dette printes ikke")

if booleansk is None:
    print("Dette printes")

booleansk = 3

if booleansk is not None:
    print("Dette printes!")

booleansk = True

if booleansk:
    print("Dette printes")