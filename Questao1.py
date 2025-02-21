# Ap2X - Questão 1


def imprimindo(guardamedia, guardaLinhas, mediaGeral):
    indice = -1
    for item in guardamedia:
        indice += 1
        if item > mediaGeral:
            print("Linha(s) com média(s) acima da Média Geral: \n", guardaLinhas[indice])


def mediaLinha(lida):
    soma = 0
    for item in lida:
        soma += int(item)
    return soma / len(lida)


def maiorValorLinhaEsoma(lida, linhasLida):
    maiorValor = int(lida[0])
    soma = 0
    for item in lida:
        soma += int(item)
        if int(item) > maiorValor:
            maiorValor = int(item)
    print("Maior da Linha", linhasLida, ":", maiorValor)
    return soma


def lendo():
    linhasLida = 0
    soma = 0
    guardamedia = []
    guardaLinhas = []
    matriz = open(arquivo, "r")
    for linha in matriz:
        linhasLida += 1
        guardaLinhas.append(linha)
        lida = linha.split()
        elementos = len(lida)  # Como é uma matriz, todas as linhas tem a mesma quantidade de elementos.
        soma += maiorValorLinhaEsoma(lida, linhasLida)
        guardamedia.append(mediaLinha(lida))
    mediaGeral = soma/(elementos * linhasLida)
    print("Média Geral:", mediaGeral)
    imprimindo(guardamedia, guardaLinhas, mediaGeral)
    matriz.close()


# Programa Principal
arquivo = input()  # Nome do arquivo: minhaMatriz.txt
lendo()