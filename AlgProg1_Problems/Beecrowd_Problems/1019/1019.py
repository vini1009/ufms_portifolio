time_input = int(input()) # Input de Horas em Segundos - Ex. de Entrada:556

hh = time_input // 3600 # Obtem a Quantia de Horas - Ex. de Saída: 0
rest = time_input % 3600 # Obtem o resto da divisão de tempo (em segundos) por horas
mm = rest // 60 # Utiliza resto divido por 60 (valor de minutos em segundos)
ss = mm % 60 # Utilize minutos (como resto) e obtem o resto por 60 (Conversão de Mins para Sec)
print("{hh}:{mm}:{ss}")