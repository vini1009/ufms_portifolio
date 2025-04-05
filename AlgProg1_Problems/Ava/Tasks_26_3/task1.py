# Solicita um número inteiro do usuário e converte a string de entrada para inteiro
any_number_input = int(input())

# Verifica se o número é par (resto da divisão por 2 é igual a 0)
if((any_number_input % 2) == 0):
    print("Par")  # Se for par, imprime "Par"
else:
    print("Impar")  # Caso contrário, imprime "Impar"