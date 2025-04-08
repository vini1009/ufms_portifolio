# Recebe as 4 notas do aluno como entrada e converte para float
n1, n2, n3, n4 = map(float, input().split())

# Calcula a média ponderada conforme os pesos especificados (2, 3, 4, 1 respectivamente)
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10.0

# Exibe a média formatada com 1 casa decimal
print(f"Media: {media:.1f}")

# Verifica a situação do aluno baseado na média
if(media >= 7.0):
    # Se média maior ou igual a 7, aluno aprovado - encerra o programa
    exit(print(f"Aluno aprovado."))
elif (media < 5.0):
    # Se média menor que 5, aluno reprovado - encerra o programa
    exit(print(f"Aluno reprovado."))
else:
    # Se média entre 5 e 6.9, aluno em exame
    print(f"Aluno em exame.")
    
    # Solicita a nota do exame
    exam = float(input())
    
    # Exibe a nota do exame
    print(f"Nota do exame: {exam}")
    
    # Calcula a média final (média aritmética entre a média original e a nota do exame)
    average_final = (media + exam) / 2
    
    # Verifica se aluno foi aprovado ou reprovado no exame
    if average_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    # Exibe a média final formatada com 1 casa decimal
    print(f"Media final: {average_final:.1f}")