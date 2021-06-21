#TALLER CONDICIONALES MINTIC - CRISTIAN MORENO 1.007.378.776
from PositiveOrNegative import isNumberPositive
from ParOrImpar import isNumberPar
from Divisible3_5 import isNumberDivisible
from CharVocal import isCharacterVocal
from CharVocalOrConsOrNumber import isCharacterCon, isCharacterNumber
from UI import userInterface, error, succes

print(userInterface("inicio","none"))
try:
  key_exercise = int(input(userInterface("options","none")))
except (ValueError, RuntimeError, TypeError, NameError):
  print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))
else:
  print(succes("succes","Se ha seleccionado el ejercicio correspondiente","SE-00"+str(key_exercise)))


if key_exercise == 1:
  #EJERCICIO 1
  print(userInterface("welcome","none"))
  print(userInterface("exercise_description","si un número es Positivo o Negativo"))
  #INPUT DATA
  try:
    input_number = float(input(userInterface("in_data","un NÚMERO para averiguar si es positivo o negativo")))
  except (Exception):
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))
  else: 
    print(succes("succes","Se ha ingresado el dato correctamente","S-002"))
  #USING METHOD
  if isNumberPositive(input_number):
      print(userInterface("number_positive",input_number))
  else :
      print(userInterface("number_negative",input_number))
  #END
elif key_exercise == 2:  
  #EJERCICIO 2
  print(userInterface("welcome","none"))
  print(userInterface("exercise_description","si un número es Par o Impar"))
  #INPUT DATA
  try:
    input_number = float(input(userInterface("in_data","un NÚMERO para averiguar si es par o impar")))
  except (Exception):
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))
  else: 
    print(succes("succes","Se ha ingresado el dato correctamente","S-002"))
  #USING METHOD
  if isNumberPar(input_number):
      print(userInterface("number_par",input_number))
  else:
      print(userInterface("number_impar",input_number))
  #END
elif key_exercise == 3:  
  #EJERCICIO 3
  print(userInterface("welcome","none"))
  print(userInterface("exercise_description","si un número es múltiplo entre 3 y 5"))
  #INPUT DATA
  try:
    input_number = float(input(userInterface("in_data","un NÚMERO para averiguar si es múltiplo de 3 y de 5")))
  except (Exception):
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))
  else: 
    print(succes("succes","Se ha ingresado el dato correctamente","S-002"))
  #USING METHOD
  if isNumberDivisible(input_number):
      print(userInterface("number_multiple3",input_number))
  else: 
    print(userInterface("number_nomultiple3",input_number))
  #END
elif key_exercise == 4:
  #EJERCICIO 4
  print(userInterface("welcome","none"))
  print(userInterface("exercise_description","si un carácter es una vocal"))
 
  input_char = input(userInterface("in_data","un CÁRACTER para empezar con el proceso"))
  if input_char.isdigit() == True:  
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001")) 
  else: 
    print(succes("succes","Se ha ingresado el dato correctamente","S-002"))  
    if isCharacterVocal(input_char):
      print(userInterface("char_vocal",input_char))
    else: print(userInterface("char_novocal",input_char))
elif key_exercise == 5:
  #UI E INPUT DE USUARIO
  print("- WELCOME -")
  print("ESTE PROGRAMA DEFINE SI UN CARACTER ES UNA VOCAL, CONSONANTE O NÚMERO:")
  input_char = input("INGRESE UNA CARACTER PARA EMPEZAR CON EL PROCESO: ")
  if isCharacterVocal(input_char):
      print("EL CARACTER: "+str(input_char)+" ES UNA VOCAL.")
  elif isCharacterNumber(input_char):
      print(" EL CARACTER: "+str(input_char)+" ES UNA NÚMERO.")
  elif isCharacterCon(input_char):
      print("EL CARACTER: "+str(input_char)+" ES UN CONSONANTE.")
  else: print("EL CARACTER: "+str(input_char)+" ES DESCONOCIDO O DE NINGUN TIPO.")


else:
  print(error("error","El número del ejercicio no se encuentra registrado.","E-002"))
