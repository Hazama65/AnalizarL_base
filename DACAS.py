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
        ' ':['E','E','E','E','E',7]
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
      token = "SW2" 
    else:
      validad = 0

    if (estadoActual == 7):
      findelinea = 0
    elif (estadoActual == 6):
      findelinea = 1

    return [validad,token,findelinea]

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
        ' ':['E','E','E','E',6]
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
      token = "SW1" 
    else:
      validad = 0

    if (estadoActual == 6):
      findelinea = 0
    elif (estadoActual == 5):
      findelinea = 1

    return [validad,token,findelinea]

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
        ' ':['E','E','E','E','E','E','E',9]
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
      token = "SW3" 
    else:
      validad = 0

    if (estadoActual == 9):
      findelinea = 0
    elif (estadoActual == 8):
      findelinea = 1

    return [validad,token,findelinea]

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
        ' ':['E','E','E', 4 ,'E','E','E','E',10]
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
      token = "SW4" 
    else:
      validad = 0

    if (estadoActual == 10):
      findelinea = 0
    elif (estadoActual == 9):
      findelinea = 1
      
    return [validad,token,findelinea]






