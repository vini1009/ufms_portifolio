n = int(input())

total_value = 0
for i in range(1, n + 1):
    total_value += 1 / i

print(f"{total_value:.4f}")