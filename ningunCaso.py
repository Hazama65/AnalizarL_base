def automata_niguno(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9]
    sigma = ['n','i','g','u','o',';',' ']
    q0= 0
    F=[8,9]
    delta = {
        'n':[1,'E',3,'E','E',6,'E'],
        'i':['E',2,'E','E','E','E','E'],
        'g':['E','E','E',4,'E','E','E'],
        'u':['E','E','E','E',5,'E','E'],
        'o':['E','E','E','E','E','E',7],
        ';':['E','E','E','E','E','E','E',8],
        ' ':['E','E','E','E','E','E','E','E',9]
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
        token = "Sw2"
    else:
        validad = 0

    if (estadoActual == 8):
        findelinea = 0
    elif (estadoActual == 9):
        findelinea = 1

    return [validad,token,findelinea]

entrada = input("Ingresa cadena a evaluar: ")
salida=automata_niguno(entrada)
print(salida)