#TALLER ESTRUCTURAS CICLICAS O BUCLES
#Cristian David Moreno - Kyonax | github.com/kyonax | kyonax@kyonax.com | 1.007.378.776
import random

def insertRandomAge (number,number_list):
  number_list.append(number)    
  number_list.sort()
  return number_list

def maxValidation (number,start,stop):
  
  return

def logicRandomAge (number,number_list,start,stop):  
  random_number = random.randint(start,stop)
  exist_number = False
  while len(number_list) != number:    
    if random_number%2 == 0:
      for i in number_list:
        if i == random_number:
          exist_number = True    

      if exist_number == False:        
        insertRandomAge(random_number,number_list)  
        random_number = random.randint(start,stop)                      
    else: random_number = random.randint(start,stop)
  return