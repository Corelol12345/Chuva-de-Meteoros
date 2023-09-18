import math

while True:
    print("-:: Sistema para Análise de Chuva de Meteoros ::-")
    print("1. Definir perímetro da propriedade e da edificação de interesse")
    print("2. Unificar sistemas de coordenadas de referência")
    print("3. Processar registros de chuva de meteoros")
    print("4. Apresentar estatísticas")
    print("5. Sair")

    op = int(input("Opção: "))
   

    if op > 3:
        break
    elif op == 5:
        break
    elif op == 1:
        f1, f2 = map(int, input('Informe o Valor de f1 e f2 da Fazenda: ').split())
        f3, f4 = map(int, input("Informe o Valor de f3 e f4 da Fazenda: ").split())
        x1, x2 = map(int, input("Informa o Valor x1, x2 da sede: ").split()) 
        y1, y2 = map(int, input('Informe o Valor de y1 e y2 da sede: ').split())
        print("Coordenadas Definidas com Exito!")
    elif op == 2:
        x, y = map(int, input("Informe as Coordenadas x e y da UPMCC: ").split())
        print("Coordenadas Definidas com Exito!")
    elif op == 3:
        while True:
            distancia = int(input("Informe a Distancia do Meteoro: "))
            if distancia < 0:
                break
            else:
                r = math.sqrt(x1**2 + x2**2)
                df = math.sqrt((f3 - f1)**2 + (f4 - f2)**2)
                dp = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)
                print(f"A Distancia Entre a Fazenda e a Propriedade:", df)
                print(f"A Distancia Entre a Fazebda e a Propriedade:", dp)