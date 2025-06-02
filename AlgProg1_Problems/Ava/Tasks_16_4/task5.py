n = int(input())

if n == 2: 
    print("Primo")
    quit()

isComposite = False

for index in range(2, int(n ** 0.5) + 1):
    if (n % index == 0):
        isComposite = True
        break

if (isComposite):
    print("Composto")
else: 
    print("Primo")