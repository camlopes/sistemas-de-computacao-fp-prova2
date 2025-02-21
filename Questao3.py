# AP2x - Questão 3

import struct
Registro = struct.Struct("f 256s")


def lendoBinario(Binario, indice):
    Binario.seek(4 + indice * Registro.size, 0)
    return Registro.unpack(Binario.read(Registro.size))


def escrevendoBinario(Binario, item, inicio):
    Binario.seek(4 + item * Registro.size, 0)
    Binario.write(Registro.pack(inicio[0], inicio[1]))


def ordenar(Binario, registros):
    for item in range(registros):
        indice = item
        inicio = lendoBinario(Binario, indice)
        for i in range(item+1, registros):
            compara = lendoBinario(Binario, i)
            # compara as palavras da tupla:
            if compara[1] < inicio[1]:
                indice = i
                inicio = compara
            # elif para quando as palavras forem iguais:
            elif compara[1] == inicio[1]:
                # comparando os numeros da tupla:
                if compara[0] < inicio[0]:
                    indice = i
                    inicio = compara
        if indice != item:
            compara = lendoBinario(Binario, item)
            escrevendoBinario(Binario, item, inicio)
            escrevendoBinario(Binario, indice, compara)


# Programa Principal
Binario = open("meuArquivo.bin", "r+b")
registros = struct.unpack("i", Binario.read(4))[0]
ordenar(Binario, registros)
Binario.close()
