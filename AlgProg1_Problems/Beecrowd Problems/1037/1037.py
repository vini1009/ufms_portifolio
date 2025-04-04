# Lê um valor numérico do usuário e converte para float (número decimal)
any_value_float = float(input())

# Verifica se o valor está fora do intervalo 0-100
if any_value_float < 0 or any_value_float > 100:
    print("Fora de intervalo")  # Imprime mensagem se estiver fora do intervalo principal

# Se o valor estiver entre 0 e 25 (inclusive)
elif any_value_float <= 25:
    print("Intervalo [0,25]")  # Notação [ ] inclui os extremos

# Se o valor estiver entre 25 (exclusive) e 50 (inclusive)
elif any_value_float <= 50:
    print("Intervalo (25,50]")  # Notação ( ) exclui o extremo inferior

# Se o valor estiver entre 50 (exclusive) e 75 (inclusive)
elif any_value_float <= 75:
    print("Intervalo (50,75]")  # Notação mista: exclui 50, inclui 75

# Se nenhuma das condições anteriores for atendida (valor entre 75 e 100)
else:
    print("Intervalo (75,100]")  # Último intervalo possível dentro do range 0-100