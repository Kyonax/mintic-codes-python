#EJERCICIO 3
#Determinar si un número es divisible por 3 y 5 al mismo tiempo, por ejemplo 15, cumple, 10 no.

#CREACION DE FUNCIONES
def isNumberDivisible(number):
    if number%3 == 0 and number%5 == 0:
        return True
    else: return False
