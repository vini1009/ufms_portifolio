a, b, c = map(float, input().split())

delta = (b ** 2) - 4 * a * c

if(a <= 0  or delta <= 0):
    print("Impossivel calcular")
else:
    r1 = (-b + (delta ** (1/2))) / (2 * a)
    r2 = (-b - (delta ** (1/2))) / (2 * a)
    print(f"R1 = {r1:.5f}")
    exit(f"R2 = {r2:.5f}")