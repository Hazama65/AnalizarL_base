import sys

# inicializar variables
def automata_inicio(cadenaEjemplo):
  token = 'N'
  findelinea = 0
  Q= [0,1,2,3,4,5,6,7,8,9]
  sigma = ['i','n','c','o',';',' ']
  q0= 0
  F=[7,8]
  delta = {
      'i':[1,'E',3,'E',5, 'E','E'],
      'n':['E',2,'E','E','E','E','E'],
      'c':['E','E','E',4,'E','E','E'],
      'o':['E','E','E','E','E',6,'E'],
      ';':['E','E','E','E','E','E',7],
      ' ':['E','E','E','E','E','E',8],
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
    token = "PR1" 
  else:
    validad = 0

  if (estadoActual == 8):
    findelinea = 0
  elif (estadoActual == 7):
    findelinea = 1

  return [validad,token,findelinea]

def automata_acaso(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7]
    sigma = ['a','c','o','s',';',' ']
    q0= 0
    F=[6,7]
    delta = {
        'a':[1,'E',3,'E','E','E'],
        'c':['E',2,'E','E','E','E'],
        's':['E','E','E',4,'E','E'],
        'o':['E','E','E','E',5,'E'],
        ';':['E','E','E','E','E',6],
        ' ':['E','E','E','E','E','E',7]
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
        token = "Sw"
    else:
        validad = 0

    if (estadoActual == 7):
        findelinea = 0
    elif (estadoActual == 6):
        findelinea = 1

    return [validad,token,findelinea]

def automata_cadena (cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4]
    sigma = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z'
    ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z',';',' ','_']
    q0= 0
    F=[3]
    delta = {
        'a': [1, 2, 2, 2, 'E', 'E'],
        'b': [1, 2, 2, 2, 'E', 'E'],
        'c': [1, 2, 2, 2, 'E', 'E'],
        'd': [1, 2, 2, 2, 'E', 'E'],
        'e': [1, 2, 2, 2, 'E', 'E'],
        'f': [1, 2, 2, 2, 'E', 'E'],
        'g': [1, 2, 2, 2, 'E', 'E'],
        'h': [1, 2, 2, 2, 'E', 'E'],
        'i': [1, 2, 2, 2, 'E', 'E'],
        'j': [1, 2, 2, 2, 'E', 'E'],
        'k': [1, 2, 2, 2, 'E', 'E'],
        'l': [1, 2, 2, 2, 'E', 'E'],
        'm': [1, 2, 2, 2, 'E', 'E'],
        'n': [1, 2, 2, 2, 'E', 'E'],
        'o': [1, 2, 2, 2, 'E', 'E'],
        'p': [1, 2, 2, 2, 'E', 'E'],
        'q': [1, 2, 2, 2, 'E', 'E'],
        'r': [1, 2, 2, 2, 'E', 'E'],
        's': [1, 2, 2, 2, 'E', 'E'],
        't': [1, 2, 2, 2, 'E', 'E'],
        'u': [1, 2, 2, 2, 'E', 'E'],
        'v': [1, 2, 2, 2, 'E', 'E'],
        'w': [1, 2, 2, 2, 'E', 'E'],
        'x': [1, 2, 2, 2, 'E', 'E'],
        'y': [1, 2, 2, 2, 'E', 'E'],
        'z': [1, 2, 2, 2, 'E', 'E'],
        'A': [1, 2, 2, 2, 'E', 'E'],
        'B': [1, 2, 2, 2, 'E', 'E'],
        'C': [1, 2, 2, 2, 'E', 'E'],
        'D': [1, 2, 2, 2, 'E', 'E'],
        'E': [1, 2, 2, 2, 'E', 'E'],
        'F': [1, 2, 2, 2, 'E', 'E'],
        'G': [1, 2, 2, 2, 'E', 'E'],
        'H': [1, 2, 2, 2, 'E', 'E'],
        'I': [1, 2, 2, 2, 'E', 'E'],
        'J': [1, 2, 2, 2, 'E', 'E'],
        'K': [1, 2, 2, 2, 'E', 'E'],
        'L': [1, 2, 2, 2, 'E', 'E'],
        'M': [1, 2, 2, 2, 'E', 'E'],
        'N': [1, 2, 2, 2, 'E', 'E'],
        'O': [1, 2, 2, 2, 'E', 'E'],
        'P': [1, 2, 2, 2, 'E', 'E'],
        'Q': [1, 2, 2, 2, 'E', 'E'],
        'R': [1, 2, 2, 2, 'E', 'E'],
        'S': [1, 2, 2, 2, 'E', 'E'],
        'T': [1, 2, 2, 2, 'E', 'E'],
        'U': [1, 2, 2, 2, 'E', 'E'],
        'V': [1, 2, 2, 2, 'E', 'E'],
        'W': [1, 2, 2, 2, 'E', 'E'],
        'X': [1, 2, 2, 2, 'E', 'E'],
        'Y': [1, 2, 2, 2, 'E', 'E'],
        'Z': [1, 2, 2, 2, 'E', 'E'],
        ' ': ['E',2,2,2,'E'],
        ';': ['E','E',3,]
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
        token = "CAD"
    else:
        validad = 0

    if (estadoActual == 2):
        findelinea = 0
    elif (estadoActual == 3):
        findelinea = 1

    return [validad,token,findelinea]

def automata_caracEsp(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2]
    sigma = ['(',')','{','}','[',']','_',',','.',';',' ']
    q0= 0
    F=[2]
    delta = {
        '(': [1, 1, 1, 'E'],
        ')': [1, 1, 1, 'E'],
        '{': [1, 1, 1, 'E'],
        '}': [1, 1, 1, 'E'],
        '[': [1, 1, 1, 'E'],
        ']': [1, 1, 1, 'E'],
        '_': [1, 1, 1, 'E'],
        ',': [1, 1, 1, 'E'],
        '.': [1, 1, 1, 'E'],
        ';': [1, 1, 1, 'E'],
        ' ':['E',2]
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
        token = "CESP"
    else:
        validad = 0

    if (estadoActual == 1):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

def automata_caso(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,]
    sigma = ['a','c','o','s',';',' ']
    q0= 0
    F=[5,6]
    delta = {
        'c':[1,'E','E','E','E'],
        'a':['E',2,'E','E','E'],
        's':['E','E',3,'E','E'],
        'o':['E','E','E',4,'E'],
        ';':['E','E','E','E',5],
        ' ':['E','E','E','E','E',6]
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
        token = "Sw1"
    else:
        validad = 0

    if (estadoActual == 6):
        findelinea = 0
    elif (estadoActual == 5):
        findelinea = 1

    return [validad,token,findelinea]

def automata_comentario(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4]
    sigma = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z',';',' ','#','_']
    q0= 0
    F=[3,4]
    delta = {
        '#': [1,'E','E','E','E','E'],
        '0': ['E', 2, 2, 2, 'E', 'E'],
        '1': ['E', 2, 2, 2, 'E', 'E'],
        '2': ['E', 2, 2, 2, 'E', 'E'],
        '3': ['E', 2, 2, 2, 'E', 'E'],
        '4': ['E', 2, 2, 2, 'E', 'E'],
        '5': ['E', 2, 2, 2, 'E', 'E'],
        '6': ['E', 2, 2, 2, 'E', 'E'],
        '7': ['E', 2, 2, 2, 'E', 'E'],
        '8': ['E', 2, 2, 2, 'E', 'E'],
        '9': ['E', 2, 2, 2, 'E', 'E'],
        'a': ['E', 2, 2, 2, 'E','E'],
        'b': ['E', 2, 2, 2, 'E','E'],
        'c': ['E', 2, 2, 2, 'E','E'],
        'd': ['E', 2, 2, 2, 'E','E'],
        'e': ['E', 2, 2, 2, 'E','E'],
        'f': ['E', 2, 2, 2, 'E','E'],
        'g': ['E', 2, 2, 2, 'E','E'],
        'h': ['E', 2, 2, 2, 'E','E'],
        'i': ['E', 2, 2, 2, 'E','E'],
        'j': ['E', 2, 2, 2, 'E','E'],
        'k': ['E', 2, 2, 2, 'E','E'],
        'l': ['E', 2, 2, 2, 'E','E'],
        'm': ['E', 2, 2, 2, 'E','E'],
        'n': ['E', 2, 2, 2, 'E','E'],
        'o': ['E', 2, 2, 2, 'E','E'],
        'p': ['E', 2, 2, 2, 'E','E'],
        'q': ['E', 2, 2, 2, 'E','E'],
        'r': ['E', 2, 2, 2, 'E','E'],
        's': ['E', 2, 2, 2, 'E','E'],
        't': ['E', 2, 2, 2, 'E','E'],
        'u': ['E', 2, 2, 2, 'E','E'],
        'v': ['E', 2, 2, 2, 'E','E'],
        'w': ['E', 2, 2, 2, 'E','E'],
        'x': ['E', 2, 2, 2, 'E','E'],
        'y': ['E', 2, 2, 2, 'E','E'],
        'z': ['E', 2, 2, 2, 'E','E'],
        '_': ['E', 2, 2, 2, 'E','E'],
        ';': ['E','E',3,],
        ' ': ['E','E','E',4]
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
        token = "CT1"
    else:
        validad = 0

    if (estadoActual == 4):
        findelinea = 0
    elif (estadoActual == 3):
        findelinea = 1

    return [validad,token,findelinea]

def automata_constantes(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3]
    sigma = ['1','2','3','4','5','6','7','8','9','0','.',';',' ']
    q0= 0
    F=[2,3]
    delta = {
        '1':[1,1],
        '2':[1,1],
        '3':[1,1],
        '4':[1,1],
        '5':[1,1],
        '6':[1,1],
        '7':[1,1],
        '8':[1,1],
        '9':[1,1],
        '0':[1,1],
        '.':[1,1],
        ';':['E',2],
        ' ':['E','E',3]
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
        token = "CONST"
    else:
        validad = 0

    if (estadoActual == 3):
        findelinea = 0
    elif (estadoActual == 2):
        findelinea = 1

    return [validad,token,findelinea]

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

def automata_fincaso(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9,10]
    sigma = ['f','i','n','c','a','s','o',';',' ']
    q0= 0
    F=[9,10]
    delta = {
        'f':[1,'E','E','E','E','E','E','E','E'],
        'i':['E',2,'E','E','E','E','E','E','E'],
        'n':['E','E',3,'E','E','E','E','E','E'],
        'c':['E','E','E','E',5,'E','E','E','E'],
        'a':['E','E','E','E','E',6,'E','E','E'],
        's':['E','E','E','E','E','E',7,'E','E'],
        'o':['E','E','E','E','E','E','E',8,'E'],
        ';':['E','E','E','E','E','E','E','E',9],
        ' ':['E','E','E',4,'E','E','E','E','E',10]
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
        token = "Sw4"
    else:
        validad = 0

    if (estadoActual == 10):
        findelinea = 0
    elif (estadoActual == 9):
        findelinea = 1

    return [validad,token,findelinea]

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

  if (estadoActual == 10):
    findelinea = 0
  elif (estadoActual == 9):
    findelinea = 1

  print(validad,token, findelinea)

def automata_hast(cadenaEjemplo):
  Q= [0,1,2,3,4,5,6,7]
  sigma = ['h','a','s','t',' ',';']
  q0= 0
  F=[6,7]
  delta = {
      'h':[1,'E','E','E','E','E','E'],
      'a':['E',2,'E','E',5,'E','E'],
      's':['E','E',3,'E','E','E','E'],
      't':['E','E','E',4,'E','E','E'],
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
    token = "HAS"
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

def automata_hasta(cadenaEjemplo):
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
      ' ':['E','E','E','E','E',6,'E'],
      ';':['E','E',3,'E','E',7,'E']
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

def automata_hasta(cadenaEjemplo):
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
      ' ':['E','E','E','E','E',6,'E'],
      ';':['E','E',3,'E','E',7,'E']
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

def automata_print(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sigma = ['p', 'r', 'i', 'n', 't', '(', ')', ' ', 'i', 'n', 'p', 'u', 't']
    q0 = 0
    F = [8]
    delta = {
        0: {'p': 1, 'i': 6, ' ': 0},
        1: {'r': 2},
        2: {'i': 3},
        3: {'n': 4},
        4: {'t': 5},
        5: {'(': 8},
        6: {'n': 7},
        7: {'p': 8},
        8: {')': 9},
        9: {' ': 0}
    }

    logitudCadena = len(cadenaEjemplo)
    estadoActual = q0

    for cabezalDeLectura in range(0, logitudCadena):
        simboloEvaluado = str(cadenaEjemplo[cabezalDeLectura])

        if simboloEvaluado in sigma:
            estadoActual = delta[estadoActual].get(simboloEvaluado, 'E')
            print(estadoActual, simboloEvaluado)

            if estadoActual == 'E':
                break
        else:
            break

    if estadoActual in F:
        validad = 1
        token = "PI"
    else:
        validad = 0

    if estadoActual == 9:
        findelinea = 0

    return [validad, token, findelinea]

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

def automata_niguno(cadenaEjemplo):
    token = 'N'
    findelinea = 0
    Q= [0,1,2,3,4,5,6,7,8,9]
    sigma = ['n','i','g','u','o',';',' ']
    q0= 0
    F=[8,9]
    delta = {
        'n':[1,'E',3,'E','E',6,'E'],
        'i':['E',2,'E','E','E','E','E'],
        'g':['E','E','E',4,'E','E','E'],
        'u':['E','E','E','E',5,'E','E'],
        'o':['E','E','E','E','E','E',7],
        ';':['E','E','E','E','E','E','E',8],
        ' ':['E','E','E','E','E','E','E','E',9]
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
        token = "Sw2"
    else:
        validad = 0

    if (estadoActual == 9):
        findelinea = 0
    elif (estadoActual == 8):
        findelinea = 1

    return [validad,token,findelinea]

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

  if (estadoActual == 7):
    findelinea = 0
  elif (estadoActual == 6):
    findelinea = 1

  print(validad,token, findelinea)




def main(argv):
    with open(argv[1]) as archivo:
        for linea in archivo:
            palabras = linea.split(' ')
            findelinea = 1
            cont = 0
            while(findelinea):
                valida = automata_inicio(palabras[cont])
                print(valida)
                findelinea = 0

if __name__ == "__main__":
  main(sys.argv)