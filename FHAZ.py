def automata_haz(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5]
  sigma = ['h','a','z',';',' ']
  q0= 0
  F=[4,5]
  delta = {
      'h':[1,'E','E','E'],
      'a':['E',2,'E','E'],
      'z':['E','E',3,'E'],
      ';':['E','E','E',4,],
      ' ':['E','E','E',5,]
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
    token = "HZ" 
  else:
    validad = 0

  if (estadoActual == 5):
    findelinea = 0
  elif (estadoActual == 4):
    findelinea = 1

  return [validad,token,findelinea]
def automata_min(cadenaEjemplo):
  token='N'
  Q= [0,1,2,3,4,5,6,7,8,9,10]
  sigma = ['m','i','e','n','t','r','a','s',' ',';']
  q0= 0
  F=[9,10]
  delta = {
      'm':[1,'E','E','E','E','E','E','E','E','E'],
      'i':['E',2,'E','E','E','E','E','E','E','E'],
      'e':['E','E',3,'E','E','E','E','E','E','E'],
      'n':['E','E','E',4,'E','E','E','E','E','E'],
      't':['E','E','E','E',5,'E','E','E','E','E'],
      'r':['E','E','E','E','E',6,'E','E','E','E'],
      'a':['E','E','E','E','E','E',7,'E','E','E'],
      's':['E','E','E','E','E','E','E',8,'E','E'],
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
    token = "MIN"
    validad = 1
  else:
    validad = 0

  if (estadoActual == 10):
    findelinea = 0
  elif (estadoActual == 9):
    findelinea = 1

  return[validad,token, findelinea]
def automata_fh(cadenaEjemplo):
  token='N'
  Q= [0,1,2,3,4,5,6,7,8]
  sigma = ['f','i','n','h','a','z',' ',';']
  q0= 0
  F=[8,7]
  delta = {
      'f':[1,'E','E','E','E','E','E','E','E','E'],
      'i':['E',2,'E','E','E','E','E','E','E','E'],
      'n':['E','E',3,'E','E','E','E','E','E','E'],
      'h':['E','E','E',4,'E','E','E','E','E','E'],
      'a':['E','E','E','E',5,'E','E','E','E','E'],
      'z':['E','E','E','E','E',6,'E','E','E','E'],
      ' ':['E','E','E','E','E','E',8,'E','E'],
      ';':['E','E','E','E','E','E',7,'E']
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
    token = "FZ"
    validad = 1
  else:
    validad = 0

  if (estadoActual == 8):
    findelinea = 0
  elif (estadoActual == 7):
    findelinea = 1

  return[validad,token, findelinea]
    
