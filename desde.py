# inicializar variables
def automata_des(cadenaEjemplo):
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
      ' ':['E','E','E','E','E',6,'E'],
      ';':['E','E','E','E','E',7,'E']
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
    print("Es una cadena valida")
    validad = 1
  else:
    print("Cadena no valida")
    validad = 0

  if (estadoActual == 7):
    findelinea = 0
  elif (estadoActual == 6):
    findelinea = 1

  print(validad,token, findelinea)


entrada = input("Ingresa cadena a evaluar: ")
salida=automata_des(entrada)