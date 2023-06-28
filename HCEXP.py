def automata_PAR1(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['(',' ']
    q0= 0
    F=[1]
    delta = {
        '(': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM1"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_PAR2(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = [')',' ']
    q0= 0
    F=[1]
    delta = {
        ')': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM2"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_LLA1(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['{',' ']
    q0= 0
    F=[1]
    delta = {
        '{': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM3"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_LLA2(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['}',' ']
    q0= 0
    F=[1]
    delta = {
        '}': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM4"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_COR1(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['[',' ']
    q0= 0
    F=[1]
    delta = {
        '[': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM5"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_COR2(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = [']',' ']
    q0= 0
    F=[1]
    delta = {
        ']': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM6"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_BJ(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['_',' ']
    q0= 0
    F=[1]
    delta = {
        '_': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM7"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_CM(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = [',',' ']
    q0= 0
    F=[1]
    delta = {
        ',': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM8"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_PT(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['.',' ']
    q0= 0
    F=[1]
    delta = {
        '.': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM9"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_PC(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = [';',' ']
    q0= 0
    F=[1]
    delta = {
        ';': [1,'E','E'],
        ' ': ['E',2],
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
        token = "SM10"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

