# Recebe o ano como entrada do usuário e converte para inteiro
year_input = int(input())

# Verifica se NÃO é divisível por 4 - primeiro critério para NÃO ser bissexto
if(year_input % 4 != 0):
    print("Ano qualquer")  # Não satisfaz o requisito básico
    
# Se for divisível por 4, verifica se NÃO é divisível por 100
elif (year_input % 100 != 0):
    print("Bissexto")  # Divisível por 4 mas não por 100 - é bissexto
    
# Se for divisível por 100, verifica se é divisível por 400
elif (year_input % 400 == 0):
    print("Bissexto")  # Divisível por 400 - é bissexto (exceção à regra do 100)
    
# Se nenhuma das condições anteriores for atendida
else:
    print("Ano qualquer")  # Divisível por 100 mas não por 400 - não é bissexto