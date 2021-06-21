#TALLER ESTRUCTURAS CICLICAS O BUCLES
#Cristian David Moreno - Kyonax | github.com/kyonax | kyonax@kyonax.com | 1.007.378.776

#IMPORTACIONES DE LA LOGICA Y LIBRERIAS
import os
from ui import defaultInterface, error, succes
from natural_numbers import logicNaturalNumbers
from multiples_of_five import logicMultiplesNumbers
from pair_numbers import logicPairNumbers  
from random_pair_age import logicRandomAge
#FINALIZACIÓN DE LOS IMPORT

#PROCESO DEL EJERCICIO #1 - Lista de los primeros Números Naturales
def naturalNumbers (number):
  number_list = []
  print(succes("succes","Se ha seleccionado el ejercicio","E-00"+str(number)))   
  print(defaultInterface("natural_n","none"))  

  try:
    number = round(float(input(defaultInterface("input","Ingrese la cantidad de números que desee mostrar por pantalla"))))    
  except:
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))   
  logicNaturalNumbers(number,number_list) 
  print(succes("finish","Primeros "+str(number)+" números naturales organizados en la siguiente lista",number_list))  
  print(defaultInterface("finish","none")) 
  return
#FINALIZACIÓN DEL EJERCICIO #1

#PROCESO DEL EJERCICIO #2 - Múltiplos de 5 y su Suma
def multiplesOfFive (number):
  number_list = []
  print(succes("succes","Se ha seleccionado el ejercicio","E-00"+str(number)))   
  print(defaultInterface("multiples_5","none"))  

  try:
    number = round(float(input(defaultInterface("input","Ingrese la cantidad de múltiplos que desee procesar en el programa"))))    
  except:
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001")) 

  number_list,suma,prom = logicMultiplesNumbers(number,number_list)
  print(succes("finish","Primeros "+str(number)+" múltiplos de 5 -> "+str(number_list)+" | SUMA -> "+str(suma)+" | PROMEDIO",str(prom)))  
  print(defaultInterface("finish","none"))
  return
#FINALIZACIÓN DEL EJERCICIO #2

#PROCESO DEL EJERCICIO #3 - Primeros Números pares
def pairNumbers (number):
  number_list = []
  print(succes("succes","Se ha seleccionado el ejercicio","E-00"+str(number)))   
  print(defaultInterface("multiples_2","none"))  

  try:
    number = round(float(input(defaultInterface("input","Ingrese la cantidad de números pares que desea mostrar en el programa"))))    
  except:
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001")) 

  logicPairNumbers(number,number_list)
  print(succes("finish","Primeros "+str(number)+" números múltiplos de 2 organizados en la siguiente lista",number_list))
  print(defaultInterface("finish","none")) 
  return
#FINALIZACIÓN DEL EJERCICIO #3

#PROCESO DEL EJERCICIO #4 - Lista de las Edades Pares - aleatorio
def ageList(number):
  number_list = []
  print(succes("succes","Se ha seleccionado el ejercicio","E-00"+str(number)))   
  print(defaultInterface("multiples_2","none"))  

  try:
    number = round(float(input(defaultInterface("input","Ingrese la cantidad de números pares que desea mostrar en el programa"))))    
  except:
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))

  try:
    start = round(float(input(defaultInterface("input","Digite el rango mínimo de edad que desea encontrar en la Lista"))))
    stop = round(float(input(defaultInterface("input","Digite el rango máximo de edad que desea encontrar en la lista"))))
  except:
    print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))

  logicRandomAge(number,number_list,start,stop)  
  print(succes("finish","Random "+str(number)+" Edades múltiplos de 2 organizados en la siguiente lista",number_list))
  print(defaultInterface("finish","none")) 
  return
#FINALIZACIÓN DEL EJERCICIO #4

#EJERCICIO NO EXISTENTE
def invalidExercise ():
  raise print(error("error","No se encuentra el ejercicio digitado","E-002"))
#FINALIZACIÓN DE LA ALERTA

#SELECCIÓN DE FUNCIONES (ejercicios)
def selectExercise (number):  
  EX = {
  1: naturalNumbers,
  2: multiplesOfFive,
  3: pairNumbers,
  4: ageList
  }
  selected = EX.get(number,invalidExercise)
  return selected(number)
#FINALIZACIÓN DE LA SELECCIÓN

#INICIO DEL PROGRAMA Y LLAMADA DE FUNCIONES
#-Interfaz del programa [Inicio]-
print(defaultInterface("welcome","none"))
print(defaultInterface("inicio","none"))
#PROCESO DEL EJERCICIO #1 - NÚMERO NATURALES
#-Try/Exception SELECCIÓN DEL EJERCICIO-
try:
  key_exercise = int(input(defaultInterface("options","none")))
except:
  print(error("error","El tipo de dato que ha sido ingresado no es correcto","E-001"))
else:
  os.system("clear")  
  selectExercise(key_exercise)





