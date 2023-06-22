# inicializar variables
def automata_fin(cadenaEjemplo):
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
      ' ':['E','E','E','E','E','E','E','E',9,'E'],
      ';':['E','E','E','E','E','E','E','E',10,'E']
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
    print("Es una cadena valida")
    validad = 1
  else:
    print("Cadena no valida")
    validad = 0

  if (estadoActual == 9):
    findelinea = 0
  elif (estadoActual == 10):
    findelinea = 1

  print(validad,token, findelinea)



entrada = input("Ingresa cadena a evaluar: ")
salida=automata_fin(entrada)