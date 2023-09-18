import math

# Inicialização de variáveis
propriedade_p1 = (0, 0)
propriedade_p2 = (0, 0)
sede = []
registros_meteoritos = []
origem_upmcc = (0, 0)

# Função para calcular as coordenadas cartesianas a partir das coordenadas polares
def coordenadas_polar_para_cartesiana(distancia, angulo):
    x = distancia * math.cos(math.radians(angulo))
    y = distancia * math.sin(math.radians(angulo))
    return x, y

# Função para verificar se um ponto está dentro do perímetro da propriedade
def ponto_dentro_propriedade(ponto, p1, p2):
    x, y = ponto
    x1, y1 = p1
    x2, y2 = p2
    return x1 <= x <= x2 and y1 <= y <= y2

# Função para verificar se houve danos à sede
def houve_danos_sede(registros_meteoritos, sede):
    for registro in registros_meteoritos:
        x, y = coordenadas_polar_para_cartesiana(registro[0], registro[1])
        if ponto_dentro_propriedade((x, y), sede[0], sede[1]):
            return True
    return False

# Menu de opções
while True:
    print("-:: Sistema para Análise de Chuva de Meteoros ::-")
    print("1. Definir perímetro da propriedade e da edificação de interesse")
    print("2. Unificar sistemas de coordenadas de referência")
    print("3. Processar registros de chuva de meteoros")
    print("4. Apresentar estatísticas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        x1, y1 = map(float, input("Digite a coordenada x e y do primeiro canto da propriedade (x1 y1): ").split())
        x2, y2 = map(float, input("Digite a coordenada x e y do segundo canto da propriedade (x2 y2): ").split())
        propriedade_p1 = (x1, y1)
        propriedade_p2 = (x2, y2)

        x_sede1, y_sede1 = map(float, input("Digite a coordenada x e y do primeiro canto da sede da fazenda (x y): ").split())
        x_sede2, y_sede2 = map(float, input("Digite a coordenada x e y do segundo canto da sede da fazenda (x y): ").split())
        sede = [(x_sede1, y_sede1), (x_sede2, y_sede2)]
    elif opcao == "2":
        distancia_upmcc = float(input("Digite a distância da UPMCC em coordenadas polares: "))
        angulo_upmcc = float(input("Digite o ângulo da UPMCC em coordenadas polares (em graus): "))
        origem_upmcc = coordenadas_polar_para_cartesiana(distancia_upmcc, angulo_upmcc)

        # Atualize a posição da propriedade
        propriedade_p1 = (propriedade_p1[0] - origem_upmcc[0], propriedade_p1[1] - origem_upmcc[1])
        propriedade_p2 = (propriedade_p2[0] - origem_upmcc[0], propriedade_p2[1] - origem_upmcc[1])

        # Atualize a posição da sede
        sede[0] = (sede[0][0] - origem_upmcc[0], sede[0][1] - origem_upmcc[1])
        sede[1] = (sede[1][0] - origem_upmcc[0], sede[1][1] - origem_upmcc[1])
    elif opcao == "3":
        registros_meteoritos = []
        queda = 0  # Contador de quedas

        while True:
            entrada = input(f"Registro #{queda + 1}\n-> Insira a distância e o ângulo (ou '-' para encerrar): ")
            if entrada == "-":
                break

            valores = entrada.split()
            if len(valores) != 2:
                print("Entrada inválida. Insira a distância e o ângulo separados por espaço.")
                continue

            distancia = float(valores[0])
            angulo = float(valores[1])
            registros_meteoritos.append((distancia, angulo))

            queda += 1
        print(f"Fim da coleta de registros: {queda} queda(s) informada(s).")
    elif opcao == "4":
        total_meteoritos = len(registros_meteoritos)
        meteoritos_na_propriedade = sum(1 for registro in registros_meteoritos if ponto_dentro_propriedade(coordenadas_polar_para_cartesiana(registro[0], registro[1]), propriedade_p1, propriedade_p2))

        # Inicialize contadores para cada quadrante
        quadrantes = {"NE": 0, "NW": 0, "SW": 0, "SE": 0}

        for registro in registros_meteoritos:
            angulo = math.degrees(registro[1])

            if 0 <= angulo < 90:
                quadrantes["NE"] += 1
            elif 90 <= angulo < 180:
                quadrantes["NW"] += 1
            elif 180 <= angulo < 270:
                quadrantes["SW"] += 1
            else:
                quadrantes["SE"] += 1

        print(f"Total de quedas registradas: {total_meteoritos} ({total_meteoritos / total_meteoritos * 100:.1f}%)")
        print(f"Quedas dentro da propriedade: {meteoritos_na_propriedade} ({meteoritos_na_propriedade / total_meteoritos * 100:.1f}%)")

        # Imprimir contagem por quadrante
        for quadrante, quantidade in quadrantes.items():
            print(f"-> Quadrante {quadrante}: {quantidade} ({quantidade / total_meteoritos * 100:.2f}%)")

        if houve_danos_sede(registros_meteoritos, sede):
            print("A edificação principal foi atingida? SIM")
        else:
            print("A edificação principal foi atingida? NÃO")
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção Invalida")
