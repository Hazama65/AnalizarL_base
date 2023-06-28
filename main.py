import sys
from conjunto import *

def main(argv):
    with open(argv[1]) as archivo:
        for linea in archivo:
            palabras = linea.split(' ')
            findelinea = 1
            cont = 0
            while(findelinea):
                valida = automata_inicio(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_fin(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_si(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_entonces(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_sino(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_finsi(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_esc(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_cap(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_acaso(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_caso(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_niguno(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_fincaso(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_des(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_hasta(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_intervalo(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_fin(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_haz(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_min(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_fh(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_ejec(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_hasta(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_PAR1(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_PAR2(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_LLA1(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_LLA2(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_COR1(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_COR2(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_BJ(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_CM(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_PT(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_PC(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_suma(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_rest(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_mult(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_div(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_exp(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_and(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_or(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_not(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_may(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_men(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_mayig(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_menig(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_difer(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_constantes(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_comentario(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_identificadores(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
                valida = automata_cadena(palabras[cont])
                if (valida[0]):
                    print (valida[1])
                    if (valida[2]):
                        findelinea = 1
                        break
if __name__ == "__main__":
  main(sys.argv)