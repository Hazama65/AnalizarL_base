def automata_caracEsp(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2]
    sigma = ['(',')','{','}','[',']','_',',','.',';',' ']
    q0= 0
    F=[2]
    delta = {
        '(': [1, 1, 1, 'E'],
        ')': [1, 1, 1, 'E'],
        '{': [1, 1, 1, 'E'],
        '}': [1, 1, 1, 'E'],
        '[': [1, 1, 1, 'E'],
        ']': [1, 1, 1, 'E'],
        '_': [1, 1, 1, 'E'],
        ',': [1, 1, 1, 'E'],
        '.': [1, 1, 1, 'E'],
        ';': [1, 1, 1, 'E'],
        ' ':['E',2]
    }
    logitudCadena = len(cadenaEjemplo)

    estadoActual = q0
    for cabezalDeLectura in range(0,logitudCadena):
        simboloEvaluado= str(cadenaEjemplo[cabezalDeLectura])
        if simboloEvaluado in sigma:
        estadoActual = delta[simboloEvaluado][estadoActual]
        print(estadoActual,simboloEvaluado)
        if(estadoActual)=='E':
            break
        else:
        break

    if (estadoActual in F):
        validad = 1
        token = "CESP"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

entrada = input("Ingresa cadena a evaluar: ")
salida=automata_caracEsp(entrada)
print(salida)