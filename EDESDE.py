def automata_des(cadenaEjemplo):
  token = 'N'
  Q= [0,1,2,3,4,5,6,7]
  sigma = ['d','e','s','D','E','S',' ',';']
  q0= 0
  F=[6,7]
  delta = {
      'd':[1,'E','E',4,'E','E','E'],
      'e':['E',2,'E','E',5,'E','E'],
      's':['E','E',3,'E','E','E','E'],
      'D':[1,'E','E',4,'E','E','E'],
      'E':['E',2,'E','E',5,'E','E'],
      'S':['E','E',3,'E','E','E','E'],
      ' ':['E','E','E','E','E',7,'E'],
      ';':['E','E','E','E','E',6,'E']
  }
  #cadenaEjemplo ='baaa'
  logitudCadena = len(cadenaEjemplo)

  estadoActual = q0
  for cabezalDeLectura in range(0,logitudCadena):
    simboloEvaluado= str(cadenaEjemplo[cabezalDeLectura])
    if simboloEvaluado in sigma:
      estadoActual = delta[simboloEvaluado][estadoActual]
      print(estadoActual)
      if(estadoActual)=='E':
        print("Cadena no valida")
        break
      #cabezalDeLectura = cabezalDeLectura+1
    else:
      print("Cadena no valida")
      break

  if (estadoActual in F):
    token = "DES"
    validad = 1
  else:
    validad = 0

  if (estadoActual == 7):
    findelinea = 0
  elif (estadoActual == 6):
    findelinea = 1

  return [validad,token,findelinea]

def automata_hasta(cadenaEjemplo):
  token = 'N'
  Q= [0,1,2,3,4,5,6,7]
  sigma = ['h','a','s','t','H','A','S','T',' ',';']
  q0= 0
  F=[6,7]
  delta = {
      'h':[1,'E','E','E','E','E','E'],
      'a':['E',2,'E','E',5,'E','E'],
      's':['E','E',3,'E','E','E','E'],
      't':['E','E','E',4,'E','E','E'],
      'H':[1,'E','E','E','E','E','E'],
      'A':['E',2,'E','E',5,'E','E'],
      'S':['E','E',3,'E','E','E','E'],
      'T':['E','E','E',4,'E','E','E'],
      ' ':['E','E','E','E','E',7,'E'],
      ';':['E','E', 3 ,'E','E',6,'E']
  }
  #cadenaEjemplo ='baaa'
  logitudCadena = len(cadenaEjemplo)

  estadoActual = q0
  for cabezalDeLectura in range(0,logitudCadena):
    simboloEvaluado= str(cadenaEjemplo[cabezalDeLectura])
    if simboloEvaluado in sigma:
      estadoActual = delta[simboloEvaluado][estadoActual]
      print(estadoActual)
      if(estadoActual)=='E':
        print("Cadena no valida")
        break
      #cabezalDeLectura = cabezalDeLectura+1
    else:
      print("Cadena no valida")
      break

  if (estadoActual in F):
    token = "HAS"

    validad = 1
  else:

    validad = 0

  if (estadoActual == 7):
    findelinea = 0
  elif (estadoActual == 6):
    findelinea = 1

  return[validad,token, findelinea]

def automata_intervalo(cadenaEjemplo):
  token = 'N'
  Q= [0,1,2,3,4,5,6,7,8,9,10,11]
  sigma = ['i','n','t','e','r','v','a','l','o',' ',';']
  q0= 0
  F=[10,11]
  delta = {
      'i':[1,'E','E','E','E','E','E','E','E','E','E'],
      'n':['E',2,'E','E','E','E','E','E','E','E','E'],
      't':['E','E',3,'E','E','E','E','E','E','E','E'],
      'e':['E','E','E',4,'E','E','E','E','E','E','E'],
      'r':['E','E','E','E',5,'E','E','E','E','E','E'],
      'v':['E','E','E','E','E',6,'E','E','E','E','E'],
      'a':['E','E','E','E','E','E',7,'E','E','E','E'],
      'l':['E','E','E','E','E','E','E',8,'E','E','E'],
      'o':['E','E','E','E','E','E','E','E',9,'E','E'],
      ' ':['E','E','E','E','E','E','E','E','E',11,'E'],
      ';':['E','E','E','E','E','E','E','E','E',10,'E']
  }
  #cadenaEjemplo ='baaa'
  logitudCadena = len(cadenaEjemplo)

  estadoActual = q0
  for cabezalDeLectura in range(0,logitudCadena):
    simboloEvaluado= str(cadenaEjemplo[cabezalDeLectura])
    if simboloEvaluado in sigma:
      estadoActual = delta[simboloEvaluado][estadoActual]
      print(estadoActual)
      if(estadoActual)=='E':
        print("Cadena no valida")
        break
      #cabezalDeLectura = cabezalDeLectura+1
    else:
      print("Cadena no valida")
      break

  if (estadoActual in F):
    token = "INTER"

    validad = 1
  else:

    validad = 0

  if (estadoActual == 11):
    findelinea = 0
  elif (estadoActual == 10):
    findelinea = 1

  return[validad,token, findelinea]

def automata_fin(cadenaEjemplo):
  token = 'N'
  Q= [0,1,2,3,4,5,6,7,8,9,10]
  sigma = ['f','i','n','d','e','s',' ',';']
  q0= 0
  F=[9,10]
  delta = {
      'f':[1,'E','E','E','E','E','E','E','E','E'],
      'i':['E',2,'E','E','E','E','E','E','E','E'],
      'n':['E','E',3,'E','E','E','E','E','E','E'],
      'd':['E','E','E',4,'E','E',7,'E','E','E'],
      'e':['E','E','E','E',5,'E','E',8,'E','E'],
      's':['E','E','E','E','E',6,'E','E','E','E'],
      ' ':['E','E','E','E','E','E','E','E',10,'E'],
      ';':['E','E','E','E','E','E','E','E',9,'E']
  }
  #cadenaEjemplo ='baaa'
  logitudCadena = len(cadenaEjemplo)

  estadoActual = q0
  for cabezalDeLectura in range(0,logitudCadena):
    simboloEvaluado= str(cadenaEjemplo[cabezalDeLectura])
    if simboloEvaluado in sigma:
      estadoActual = delta[simboloEvaluado][estadoActual]
      print(estadoActual)
      if(estadoActual)=='E':
        print("Cadena no valida")
        break
      #cabezalDeLectura = cabezalDeLectura+1
    else:
      print("Cadena no valida")
      break

  if (estadoActual in F):
    token = "FDES"
    validad = 1
  else:
    validad = 0

  if (estadoActual == 10):
    findelinea = 0
  elif (estadoActual == 9):
    findelinea = 1

  return[validad,token, findelinea]












