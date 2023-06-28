def automata_constantes(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['1','2','3','4','5','6','7','8','9','0','.',';',' ']
    q0= 0
    F=[2,3]
    delta = {
        '1':[1,1],
        '2':[1,1],
        '3':[1,1],
        '4':[1,1],
        '5':[1,1],
        '6':[1,1],
        '7':[1,1],
        '8':[1,1],
        '9':[1,1],
        '0':[1,1],
        '.':[1,1],
        ';':['E',2],
        ' ':['E',3]
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
        token = "CONST"
    else:
        validad = 0

    if (estadoActual == 3):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]
