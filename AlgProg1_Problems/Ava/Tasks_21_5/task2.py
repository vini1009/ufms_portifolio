
def getLists():
    u = input().split()
    v = input().split()
    return u, v

def calcProduct(lists):
    finalResult = 0

    for index in range(0, len(lists[0])):
        index = int(index - 1)
        finalResult += float(lists[0][index]) * float (lists[1][index])

    print(f"{finalResult:.4f}")


def main():
    u, v = getLists()
    calcProduct([u, v])
    
main()