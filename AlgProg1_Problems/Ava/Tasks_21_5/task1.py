
def sort(list):
    list = (list.split())

    last = 0
    minValue = False
    maxValue = False
    for i in list:
        # print(i)
        i = int(i)
        
        isFirstAccess = True if minValue == False else False
        
        if(isFirstAccess):
            minValue = i
            maxValue = i
        
        if (i > minValue and i >= maxValue):
            maxValue = i
            continue
        if (i < minValue):
            minValue = i
            
    return [minValue, maxValue]

def showResult(results):
    print(f"Menor = {results[0]}")
    print(f"Maior = {results[1]}")

def main():
    results = sort(input())
    showResult(results)
main()