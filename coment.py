def automata_comentario(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4]
    sigma = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z',';',' ','#','_']
    q0= 0
    F=[3,4]
    delta = {
        '#': [1,'E','E','E','E','E'],
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
        'a': ['E', 2, 2, 2, 'E','E'],
        'b': ['E', 2, 2, 2, 'E','E'],
        'c': ['E', 2, 2, 2, 'E','E'],
        'd': ['E', 2, 2, 2, 'E','E'],
        'e': ['E', 2, 2, 2, 'E','E'],
        'f': ['E', 2, 2, 2, 'E','E'],
        'g': ['E', 2, 2, 2, 'E','E'],
        'h': ['E', 2, 2, 2, 'E','E'],
        'i': ['E', 2, 2, 2, 'E','E'],
        'j': ['E', 2, 2, 2, 'E','E'],
        'k': ['E', 2, 2, 2, 'E','E'],
        'l': ['E', 2, 2, 2, 'E','E'],
        'm': ['E', 2, 2, 2, 'E','E'],
        'n': ['E', 2, 2, 2, 'E','E'],
        'o': ['E', 2, 2, 2, 'E','E'],
        'p': ['E', 2, 2, 2, 'E','E'],
        'q': ['E', 2, 2, 2, 'E','E'],
        'r': ['E', 2, 2, 2, 'E','E'],
        's': ['E', 2, 2, 2, 'E','E'],
        't': ['E', 2, 2, 2, 'E','E'],
        'u': ['E', 2, 2, 2, 'E','E'],
        'v': ['E', 2, 2, 2, 'E','E'],
        'w': ['E', 2, 2, 2, 'E','E'],
        'x': ['E', 2, 2, 2, 'E','E'],
        'y': ['E', 2, 2, 2, 'E','E'],
        'z': ['E', 2, 2, 2, 'E','E'],
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
        token = "CT1"
    else:
        validad = 0

    if (estadoActual == 3):
        findelinea = 0
    elif (estadoActual == 4):
        findelinea = 1

    return [validad,token,findelinea]

entrada = input("Ingresa cadena a evaluar: ")
salida=automata_comentario(entrada)
print(salida)