import sys


def automata_print(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sigma = ['p', 'r', 'i', 'n', 't', '(', ')', ' ', 'i', 'n', 'p', 'u', 't']
    q0 = 0
    F = [8]
    delta = {
        0: {'p': 1, 'i': 6, ' ': 0},
        1: {'r': 2},
        2: {'i': 3},
        3: {'n': 4},
        4: {'t': 5},
        5: {'(': 8},
        6: {'n': 7},
        7: {'p': 8},
        8: {')': 9},
        9: {' ': 0}
    }

    logitudCadena = len(cadenaEjemplo)
    estadoActual = q0

    for cabezalDeLectura in range(0, logitudCadena):
        simboloEvaluado = str(cadenaEjemplo[cabezalDeLectura])

        if simboloEvaluado in sigma:
            estadoActual = delta[estadoActual].get(simboloEvaluado, 'E')
            print(estadoActual, simboloEvaluado)

            if estadoActual == 'E':
                break
        else:
            break

    if estadoActual in F:
        validad = 1
        token = "PI"
    else:
        validad = 0

    if estadoActual == 9:
        findelinea = 0

    return [validad, token, findelinea]


def main(argv):
    with open(argv[1]) as archivo:
        for linea in archivo:
            palabras = linea.split(' ')
            findelinea = 1
            cont = 0

            while findelinea:
                valida = automata_print(palabras[cont])
                print(valida)
                findelinea = 0


if __name__ == "__main__":
    main(sys.argv)
