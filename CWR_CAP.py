def automata_esc(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9]
    sigma = ['e','s','c','r','i','b',';',' ']
    q0= 0
    F=[8,9]
    delta = {
        'e':[1,'E','E','E','E','E',7],
        's':['E',2,'E','E','E','E','E'],
        'c':['E','E',3,'E','E','E','E'],
        'r':['E','E','E',4,'E','E','E'],
        'i':['E','E','E','E',5,'E','E'],
        'b':['E','E','E','E','E',6,'E'],
        ';':['E','E','E','E','E','E','E',8],
        ' ':['E','E','E','E','E','E','E',9],
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
      token = "WR" 
    else:
      validad = 0

    if (estadoActual == 9):
      findelinea = 0
    elif (estadoActual == 8):
      findelinea = 1

    return [validad,token,findelinea]

def automata_cap(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9]
    sigma = ['c','a','p','t','u','r',';',' ']
    q0= 0
    F=[8,9]
    delta = {
        'c':[1,'E','E','E','E','E','E'],
        'a':['E',2,'E','E','E','E',7],
        'p':['E','E',3,'E','E','E','E'],
        't':['E','E','E',4,'E','E','E'],
        'u':['E','E','E','E',5,'E','E'],
        'r':['E','E','E','E','E',6,'E'],
        ';':['E','E','E','E','E','E','E',8],
        ' ':['E','E','E','E','E','E','E',9],
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
      token = "CAP"
    else:
      validad = 0

    if (estadoActual == 9):
      findelinea = 0
    elif (estadoActual == 8):
      findelinea = 1

    return [validad,token,findelinea]