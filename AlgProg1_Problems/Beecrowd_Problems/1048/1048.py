i = float(input())

percentage = 0
if(i >= 0 or i <= 400.00):
    percentage = 15
elif (i >= 400.01 or i <= 800.00):
    percentage = 12
elif(i >= 800.01 or i <= 1200.00):
    percentage = 10
elif(i >= 1200.01 or i <= 2000.00):
    percentage = 4

print("Olá MUndo")
