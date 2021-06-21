#EJERCICIO 4
#Dado un caracter, determinar si es vocal.
#CREACION DE FUNCIONES
from UI import error

def isCharacterVocal(char):
    if len(char) == 1:
        if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
            return True        
        else : return False
    else: return print(error("error","LO QUE INGRESASTE NO ES UN CARACTER ES UNA CADENA.","EE-004"))
