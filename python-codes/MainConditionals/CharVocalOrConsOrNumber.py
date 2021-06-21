#EJERCICIO 5
#Dado un caracter, determinar si es vicakm consonante o digito númerico.
#CREACION DE FUNCIONES
from CharVocal import isCharacterVocal

def isCharacterNumber(char):
    if char.isdigit():
        return True
    else: return False

def isCharacterCon(char):
    if isCharacterVocal(char) and isCharacterNumber(char):
        return False
    else: return True

