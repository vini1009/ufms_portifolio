
'''
#
# Lógica de resolução
#
# a > b e a > c -> a é o maior -> nada
# b > a e b > c -> b é maior -> trocar a com b
# c > a e c > b -> c é o maior -> trocar a com c
#
'''

a, b, c = map(float, input().split())

if (b > a and b > c):
    # 'b' é o maior
    temp = a 
    a = b
    c = temp
elif c > a and c > b:
    # 'C' é o maior
    # temp = 

