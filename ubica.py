# inicializar variables
def automata_ubica(cadenaEjemplo):
  Q= [0,1,2,3,4,5,6,7]
  sigma = ['u','b','i','c','a',' ',';']
  q0= 0
  F=[6,7]
  delta = {
      'u':[1,'E','E','E','E','E','E'],
      'b':['E',2,'E','E','E','E','E'],
      'i':['E','E',3,'E','E','E','E'],
      'c':['E','E','E',4,'E','E','E'],
      'a':['E','E','E','E',5,'E','E'],
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
    token = "UBI"
    print("Es una cadena valida")
    validad = 1
  else:
    print("Cadena no valida")
    validad = 0

  if (estadoActual == 6):
    findelinea = 0
  elif (estadoActual == 7):
    findelinea = 1

  print(validad,token, findelinea)



entrada = input("Ingresa cadena a evaluar: ")
salida=automata_ubica(entrada)