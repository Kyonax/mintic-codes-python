#EJERCICIO NÚMERO 1 - MinTIC | Taller Bucles
#Archivo de Logica | By: Cristian Moreno - Kyonax | kyonax@kyonax.com | 1.007.378.776
def insertNaturalNumbers (number,number_list):  
  number_list.append(number)    
  number_list.sort()
  return number_list

def logicNaturalNumbers (number,number_list):    
  iterator = 0  
  while iterator != number:        
    insertNaturalNumbers(iterator+1,number_list) 
    iterator = iterator+1    
  return
