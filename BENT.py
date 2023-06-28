def automata_si(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4]
  sigma = ['s','i',';',' ']
  q0= 0
  F=[4,3]
  delta = {
      's':[1,'E','E','E'],
      'i':['E',2,'E','E'],
      ';':['E','E',3],
      ' ':['E','E',4]
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
    token = "Y" 
  else:
    validad = 0

  if (estadoActual == 4):
    findelinea = 0
  elif (estadoActual == 3):
    findelinea = 1

  return [validad,token,findelinea]

def automata_entonces(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9,10]
    sigma = ['e','n','t','o','c','s',';',' ']
    q0= 0
    F=[10,9]
    delta = {
        'e':[ 1 ,'E','E','E','E','E', 7 ,'E'],
        'n':['E', 2 ,'E','E', 5 ,'E','E','E'],
        't':['E','E', 3 ,'E','E','E','E','E'],
        'o':['E','E','E', 4 ,'E','E','E','E'],
        'c':['E','E','E','E','E', 6 ,'E','E'],
        's':['E','E','E','E','E','E','E', 8 ],
        ';':['E','E','E','E','E','E','E','E',9],
        ' ':['E','E','E','E','E','E','E','E',10]
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
      token = "ENT" 
    else:
      validad = 0

    if (estadoActual == 10):
      findelinea = 0
    elif (estadoActual == 9):
      findelinea = 1

    return [validad,token,findelinea]

def automata_sino(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5,6]
  sigma = ['s','i','n','o',';',' ']
  q0= 0
  F=[5,6]
  delta = {
      's':[1,'E','E','E'],
      'i':['E',2,'E','E'],
      'n':['E','E',3,'E'],
      'o':['E','E','E',4],
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
    token = "YN" 
  else:
    validad = 0

  if (estadoActual == 6):
    findelinea = 0
  elif (estadoActual == 5):
    findelinea = 1

  return [validad,token,findelinea]

def automata_finsi(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5,6,7]
  sigma = ['f','i','n','s',';',' ']
  q0= 0
  F=[6,7]
  delta = {
      'f':[1,'E','E','E'],
      'i':['E',2,'E','E',5],
      'n':['E','E',3,'E'],
      's':['E','E','E',4],
      ';':['E','E','E','E','E',6],
      ' ':['E','E','E','E','E',7],
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
    token = "FS" 
  else:
    validad = 0

  if (estadoActual == 7):
    findelinea = 0
  elif (estadoActual == 6):
    findelinea = 1

  return [validad,token,findelinea]