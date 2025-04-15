value_input = 172

if(value_input == 0):
    print("1 digitos")
    quit()

i = 0
calc = value_input
counter = 0
pause = False
while(pause != True):
    calc = calc / 10
    if (calc > 0):
        counter += 1
    else:
        pause = True

print(counter)