n = int(input())

for i in range(1, n + 1):
    
    isThreeMultiple = True if i % 3 == 0 else False
    isFiveMultiple = True if i % 5 == 0 else False

    result = ""

    if(isThreeMultiple):
        result += "Fizz"
    
    if(isFiveMultiple):
        result += "Buzz"

    if(not isThreeMultiple and not isFiveMultiple):
        result = i

    print(result)