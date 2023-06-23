# inicializar variables
def automata_limpia(cadenaEjemplo):
  Q= [0,1,2,3,4,5,6,7,8]
  sigma = ['l','i','m','p','a',' ',';']
  q0= 0
  F=[7,8]
  delta = {
      'l':[1,'E','E','E','E','E','E','E'],
      'i':['E',2,'E','E',5,'E','E','E'],
      'm':['E','E',3,'E','E','E','E','E'],
      'p':['E','E','E',4,'E','E','E','E'],
      'a':['E','E','E','E','E',6,'E','E'],
      ' ':['E','E','E','E','E','E',7,'E'],
      ';':['E','E','E','E','E','E',8,'E']
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
    token = "LIM"
    print("Es una cadena valida")
    validad = 1
  else:
    print("Cadena no valida")
    validad = 0

  if (estadoActual == 8):
    findelinea = 0
  elif (estadoActual == 7):
    findelinea = 1

  print(validad,token, findelinea)


entrada = input("Ingresa cadena a evaluar: ")
salida=automata_limpia(entrada)