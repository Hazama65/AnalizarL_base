def automata_acaso(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7]
    sigma = ['a','c','o','s',';',' ']
    q0= 0
    F=[6,7]
    delta = {
        'a':[1,'E',3,'E','E','E'],
        'c':['E',2,'E','E','E','E'],
        's':['E','E','E',4,'E','E'],
        'o':['E','E','E','E',5,'E'],
        ';':['E','E','E','E','E',6],
        ' ':['E','E','E','E','E','E',7]
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
        token = "Sw"
    else:
        validad = 0

    if (estadoActual == 7):
        findelinea = 0
    elif (estadoActual == 6):
        findelinea = 1

    return [validad,token,findelinea]


entrada = input("Ingresa cadena a evaluar: ")
salida=automata_acaso(entrada)
print(salida)