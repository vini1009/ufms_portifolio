# Animal - Resolução

p1 = input()
p2 = input()
p3 = input()

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        # mamifero
        if p3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    # invertebrado
    if p2 == "inseto":
        if p3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if p3 == "hematofago":
            print("sanguessuga")
        else:
            # Onivoro
            print("minhoca")