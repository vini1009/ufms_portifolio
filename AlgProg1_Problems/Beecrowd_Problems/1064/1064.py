# Números pares

i = 1
positiveCount = 0
m = 0

while (i <= 6):
    value_input = float(input())
    if (value_input > 0):
        positiveCount += 1
        m += value_input
    i += 1

print(f"{positiveCount} valores positivos")

m = m / positiveCount

print(f"{m:.1f}")