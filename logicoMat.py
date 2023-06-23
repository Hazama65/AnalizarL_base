def automata_suma(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['+',' ']
    q0= 0
    F=[2]
    delta = {
        '+': [1,'E','E'],
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
        token = "SUM"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_rest(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['-',' ']
    q0= 0
    F=[2]
    delta = {
        '-': [1,'E','E'],
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
        token = "RES"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_mult(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['*',' ']
    q0= 0
    F=[2]
    delta = {
        '*': [1,'E','E'],
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
        token = "MUL"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_div(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['/',' ']
    q0= 0
    F=[2]
    delta = {
        '/': [1,'E','E'],
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
        token = "DIV"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_exp(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['^',' ']
    q0= 0
    F=[2]
    delta = {
        '^': [1,'E','E'],
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
        token = "EXP"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_and(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['&',' ']
    q0= 0
    F=[2]
    delta = {
        '&': [1,'E','E'],
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
        token = "AND"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_or(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['~',' ']
    q0= 0
    F=[2]
    delta = {
        '~': [1,'E','E'],
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
        token = "OR"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_not(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['!',' ']
    q0= 0
    F=[2]
    delta = {
        '!': [1,'E','E'],
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
        token = "NOT"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_may(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['>',' ']
    q0= 0
    F=[2]
    delta = {
        '>': [1,'E','E'],
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
        token = "MAY"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_men(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['>',' ']
    q0= 0
    F=[2]
    delta = {
        '<': [1,'E','E'],
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
        token = "MEN"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_mayig(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['>','=',' ']
    q0= 0
    F=[3]
    delta = {
        '>': [1,'E','E'],
        '=': ['E',2,'E'],
        ' ': ['E','E',3],
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
        token = "MAYIGU"
    else:
        validad = 0

    if (estadoActual == 2):
        findelinea = 0
    elif (estadoActual == 3):
        findelinea = 1

    return [validad,token,findelinea]

def automata_menig(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['<','=',' ']
    q0= 0
    F=[3]
    delta = {
        '<': [1,'E','E'],
        '=': ['E',2,'E'],
        ' ': ['E','E',3],
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
        token = "MENIGU"
    else:
        validad = 0

    if (estadoActual == 2):
        findelinea = 0
    elif (estadoActual == 3):
        findelinea = 1

    return [validad,token,findelinea]

def automata_difer(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['>','<',' ']
    q0= 0
    F=[3]
    delta = {
        '<': [1,'E','E'],
        '>': ['E',2,'E'],
        ' ': ['E','E',3],
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
        token = "DIF"
    else:
        validad = 0

    if (estadoActual == 2):
        findelinea = 0
    elif (estadoActual == 3):
        findelinea = 1

    return [validad,token,findelinea]






