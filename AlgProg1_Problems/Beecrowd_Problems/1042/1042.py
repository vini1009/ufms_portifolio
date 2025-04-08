"""

Continuar em Casa

"""

a, b, c = map(int, input().split())

if(a > b): 
    if (b > c):
        print(f"{c}\n{b}\n{a}")
        # A é maior que B, e B é maior que C | Resultado : C,B,A
    else:
        # A é maior que B, e C é maior que B | Resultado: B, 
        print(f"")