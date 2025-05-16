x = 2.4
k = 4

isSum = False

if(k % 2 == 0):

    calcResult = False  # A variável calcResult é inicializada como False

    for i in range(2, k + 1, 2):  # Loop sobre os números 2, 4
        print(f"{i}")

        fator = 1
        for j in range(2, i + 1):
            fator *= j

        localCalc = x * i / fator  # Calcula o valor de localCalc para cada i

        if(calcResult == False):  # Se calcResult ainda for False (inicialmente)
            calcResult = localCalc  # Atribui o valor de localCalc a calcResult
        else:
            if(isSum):  # Se isSum for True, soma o valor
                calcResult += localCalc  # Atualiza calcResult com a soma
            else:  # Se isSum for False, subtrai o valor
                calcResult -= localCalc  # Atualiza calcResult com a subtração

        print(f"Fator: {fator} | Resultado 1 : {localCalc:.4f}")
        
    isSum = not isSum  # Inverte o valor de isSum

    calcResult *= -1  # Multiplica calcResult por -1

    print(f"Resultadão: {calcResult:.4f}")
