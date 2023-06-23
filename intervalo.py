# inicializar variables
def automata_intervalo(cadenaEjemplo):
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
      ' ':['E','E','E','E','E','E','E','E','E',10,'E'],
      ';':['E','E','E','E','E','E','E','E','E',11,'E']
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
    print("Es una cadena valida")
    validad = 1
  else:
    print("Cadena no valida")
    validad = 0

  if (estadoActual == 11):
    findelinea = 0
  elif (estadoActual == 10):
    findelinea = 1

  print(validad,token, findelinea)



entrada = input("Ingresa cadena a evaluar: ")
salida=automata_intervalo(entrada)