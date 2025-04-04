# Recebe as escolhas do usuário, converte para maiúsculas e separa em uma lista
choices = input().upper().split()

# Preços base para cada tamanho de pizza
pizza_size_p = 15.00  # Pizza pequena
pizza_size_m = 18.50  # Pizza média
pizza_size_g = 23.00  # Pizza grande

# Preços para adicionais
extra_cheese_size_p = 2.50    # Queijo extra para pizza pequena
extra_cheese_size_default = 4.00  # Queijo extra para outros tamanhos
extra_border_price = 5.00     # Borda recheada

price = 0.00  # Inicializa o preço total

# Verifica o tamanho da pizza (primeira escolha)
if(choices[0] == 'P'):
    price += pizza_size_p
elif (choices[0] == 'M'):
     price += pizza_size_m
elif (choices[0] == 'G'):
     price += pizza_size_g

# Verifica se quer queijo extra (segunda escolha)
if(choices[1] == 'S'):
        if(choices[0] == 'P'):
            price += extra_cheese_size_p
        else:
            price += extra_cheese_size_default

# Verifica se quer borda recheada (terceira escolha)
if(choices[2] == 'S'):
    price += extra_border_price

# Exibe o preço total formatado com 2 casas decimais
print(f"Total: R$ {price:.2f}")