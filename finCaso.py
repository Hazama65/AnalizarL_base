def automata_fincaso(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9,10]
    sigma = ['f','i','n','c','a','s','o',';',' ']
    q0= 0
    F=[9,10]
    delta = {
        'f':[1,'E','E','E','E','E','E','E','E'],
        'i':['E',2,'E','E','E','E','E','E','E'],
        'n':['E','E',3,'E','E','E','E','E','E'],
        'c':['E','E','E','E',5,'E','E','E','E'],
        'a':['E','E','E','E','E',6,'E','E','E'],
        's':['E','E','E','E','E','E',7,'E','E'],
        'o':['E','E','E','E','E','E','E',8,'E'],
        ';':['E','E','E','E','E','E','E','E',9],
        ' ':['E','E','E',4,'E','E','E','E','E',10]
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
        token = "Sw4"
    else:
        validad = 0

    if (estadoActual == 10):
        findelinea = 0
    elif (estadoActual == 9):
        findelinea = 1

    return [validad,token,findelinea]

entrada = input("Ingresa cadena a evaluar: ")
salida=automata_fincaso(entrada)
print(salida)