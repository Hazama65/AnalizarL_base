def automata_caso(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,]
    sigma = ['a','c','o','s',';',' ']
    q0= 0
    F=[5,6]
    delta = {
        'c':[1,'E','E','E','E'],
        'a':['E',2,'E','E','E'],
        's':['E','E',3,'E','E'],
        'o':['E','E','E',4,'E'],
        ';':['E','E','E','E',5],
        ' ':['E','E','E','E','E',6]
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
        token = "Sw1"
    else:
        validad = 0

    if (estadoActual == 5):
        findelinea = 0
    elif (estadoActual == 6):
        findelinea = 1

    return [validad,token,findelinea]

entrada = input("Ingresa cadena a evaluar: ")
salida=automata_caso(entrada)
print(salida)