def automata_identificadores (cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4]
    sigma = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z'
    ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z',';',' ','_']
    q0= 0
    F=[3,4]
    delta = {
        '0': ['E', 2, 2, 2, 'E', 'E'],
        '1': ['E', 2, 2, 2, 'E', 'E'],
        '2': ['E', 2, 2, 2, 'E', 'E'],
        '3': ['E', 2, 2, 2, 'E', 'E'],
        '4': ['E', 2, 2, 2, 'E', 'E'],
        '5': ['E', 2, 2, 2, 'E', 'E'],
        '6': ['E', 2, 2, 2, 'E', 'E'],
        '7': ['E', 2, 2, 2, 'E', 'E'],
        '8': ['E', 2, 2, 2, 'E', 'E'],
        '9': ['E', 2, 2, 2, 'E', 'E'],
        'a': [1, 2, 2, 2, 'E', 'E'],
        'b': [1, 2, 2, 2, 'E', 'E'],
        'c': [1, 2, 2, 2, 'E', 'E'],
        'd': [1, 2, 2, 2, 'E', 'E'],
        'e': [1, 2, 2, 2, 'E', 'E'],
        'f': [1, 2, 2, 2, 'E', 'E'],
        'g': [1, 2, 2, 2, 'E', 'E'],
        'h': [1, 2, 2, 2, 'E', 'E'],
        'i': [1, 2, 2, 2, 'E', 'E'],
        'j': [1, 2, 2, 2, 'E', 'E'],
        'k': [1, 2, 2, 2, 'E', 'E'],
        'l': [1, 2, 2, 2, 'E', 'E'],
        'm': [1, 2, 2, 2, 'E', 'E'],
        'n': [1, 2, 2, 2, 'E', 'E'],
        'o': [1, 2, 2, 2, 'E', 'E'],
        'p': [1, 2, 2, 2, 'E', 'E'],
        'q': [1, 2, 2, 2, 'E', 'E'],
        'r': [1, 2, 2, 2, 'E', 'E'],
        's': [1, 2, 2, 2, 'E', 'E'],
        't': [1, 2, 2, 2, 'E', 'E'],
        'u': [1, 2, 2, 2, 'E', 'E'],
        'v': [1, 2, 2, 2, 'E', 'E'],
        'w': [1, 2, 2, 2, 'E', 'E'],
        'x': [1, 2, 2, 2, 'E', 'E'],
        'y': [1, 2, 2, 2, 'E', 'E'],
        'z': [1, 2, 2, 2, 'E', 'E'],
        'A': [1, 2, 2, 2, 'E', 'E'],
        'B': [1, 2, 2, 2, 'E', 'E'],
        'C': [1, 2, 2, 2, 'E', 'E'],
        'D': [1, 2, 2, 2, 'E', 'E'],
        'E': [1, 2, 2, 2, 'E', 'E'],
        'F': [1, 2, 2, 2, 'E', 'E'],
        'G': [1, 2, 2, 2, 'E', 'E'],
        'H': [1, 2, 2, 2, 'E', 'E'],
        'I': [1, 2, 2, 2, 'E', 'E'],
        'J': [1, 2, 2, 2, 'E', 'E'],
        'K': [1, 2, 2, 2, 'E', 'E'],
        'L': [1, 2, 2, 2, 'E', 'E'],
        'M': [1, 2, 2, 2, 'E', 'E'],
        'N': [1, 2, 2, 2, 'E', 'E'],
        'O': [1, 2, 2, 2, 'E', 'E'],
        'P': [1, 2, 2, 2, 'E', 'E'],
        'Q': [1, 2, 2, 2, 'E', 'E'],
        'R': [1, 2, 2, 2, 'E', 'E'],
        'S': [1, 2, 2, 2, 'E', 'E'],
        'T': [1, 2, 2, 2, 'E', 'E'],
        'U': [1, 2, 2, 2, 'E', 'E'],
        'V': [1, 2, 2, 2, 'E', 'E'],
        'W': [1, 2, 2, 2, 'E', 'E'],
        'X': [1, 2, 2, 2, 'E', 'E'],
        'Y': [1, 2, 2, 2, 'E', 'E'],
        'Z': [1, 2, 2, 2, 'E', 'E'],
        '_': ['E', 2, 2, 2, 'E','E'],
        ';': ['E','E',3,],
        ' ': ['E','E','E',4]
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
        token = "IDE"
    else:
        validad = 0

    if (estadoActual == 3):
        findelinea = 0
    elif (estadoActual == 4):
        findelinea = 1

    return [validad,token,findelinea]

entrada = input("Ingresa cadena a evaluar: ")
salida=automata_identificadores(entrada)
print(salida)