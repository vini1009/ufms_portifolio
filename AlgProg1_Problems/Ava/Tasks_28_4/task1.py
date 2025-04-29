n = int(input())
i = 3
pi = 4
progressivo = 0
isPlus = False

while i <= n:
    if(not(isPlus)):
        isPlus = True
        progressivo -= 4/i
    else: 
        isPlus = False
        progressivo += 4/i
    i += 2

pi = pi - (progressivo * -1)
print(f"{pi:.4f}")
        
