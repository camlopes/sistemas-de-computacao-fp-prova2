# Ap2X - Questão 2

listaDistancia = []  # Guarda as somas feitas em distancia()


def distancia(coordenadas, telefone):
    guardaDistancia = 0
    for item in range(len(coordenadas)-1):
        guardaDistancia += ((float(coordenadas[item][0]) - float(coordenadas[item+1][0]))**2 + (float(coordenadas[item][1]) - float(coordenadas[item+1][1]))**2)**0.5
    listaDistancia.append(guardaDistancia)
    if guardaDistancia > 500:
        print(telefone, "percorreu:", guardaDistancia, "metros")


def lendoPontos(telefone):
    coordenadas = []
    tel = open(telefone + ".txt", "r")
    for linha in tel:
        pontos = linha.strip("\n").split()
        coordenadas.append(pontos)
    tel.close()
    distancia(coordenadas, telefone)


def lendo():
    cidade = open(arquivo, "r")
    for linha in cidade:
        telefone = linha.strip("\n")
        lendoPontos(telefone)
    cidade.close()


# Programa Principal
arquivo = input()   # Nome do arquivo: "paris.txt"
lendo()
media = 0
for item in range(len(listaDistancia)):
    media += listaDistancia[item]
print("Média das Distâncias Percorridas:", media / len(listaDistancia))