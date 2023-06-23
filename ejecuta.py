# inicializar variables
def automata_ejec(cadenaEjemplo):
  Q= [0,1,2,3,4,5,6,7,8,9]
  sigma = ['e','j','c','u','t','a',' ',';']
  q0= 0
  F=[8,9]
  delta = {
      'e':[1,'E',3,'E','E','E','E','E','E'],
      'j':['E',2,'E','E','E','E','E','E','E'],
      'c':['E','E','E',4,'E','E','E','E','E'],
      'u':['E','E','E','E',5,'E','E','E','E'],
      't':['E','E','E','E','E',6,'E','E','E'],
      'a':['E','E','E','E','E','E',7,'E','E'],
      ' ':['E','E','E','E','E','E','E',8,'E'],
      ';':['E','E','E','E','E','E','E',9,'E']
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
    token = "EJE"
    print("Es una cadena valida")
    validad = 1
  else:
    print("Cadena no valida")
    validad = 0

  if (estadoActual == 9):
    findelinea = 0
  elif (estadoActual == 8):
    findelinea = 1

  print(validad,token, findelinea)


entrada = input("Ingresa cadena a evaluar: ")
salida=automata_ejec(entrada)