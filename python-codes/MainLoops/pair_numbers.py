#EJERCICIO NÚMERO 2 - MinTIC | Taller Bucles
#Archivo de Logica | By: Cristian Moreno - Kyonax | kyonax@kyonax.com | 1.007.378.776
def insertPairNumbers (number,number_list):
  number_list.append(number)    
  number_list.sort()
  return number_list

def logicPairNumbers (number,number_list):
  iterator = 1  
  while len(number_list) != number:     
    if iterator%2 == 0:
      insertPairNumbers(iterator,number_list)  
      iterator = iterator+1
    else: iterator = iterator+1        
  return 