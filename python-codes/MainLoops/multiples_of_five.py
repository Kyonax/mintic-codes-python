#EJERCICIO NÚMERO 2 - MinTIC | Taller Bucles
#Archivo de Logica | By: Cristian Moreno - Kyonax | kyonax@kyonax.com | 1.007.378.776
def insertMultiplesNumbers (number,number_list):
  number_list.append(number)    
  number_list.sort()
  return number_list

def sumMultiplesNumbers (number_list):
  result = 0
  for i in number_list:
    result = result+i    
  return result

def promMultiplesNumbers (number_list): 
  return sumMultiplesNumbers(number_list)/len(number_list)

def logicMultiplesNumbers (number,number_list):
  iterator = 1  
  while len(number_list) != number:     
    if iterator%5 == 0:
      insertMultiplesNumbers(iterator,number_list)  
      iterator = iterator+1
    else: iterator = iterator+1        
  return number_list,sumMultiplesNumbers(number_list),promMultiplesNumbers(number_list)