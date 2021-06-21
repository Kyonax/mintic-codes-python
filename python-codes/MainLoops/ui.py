#INTERFAZ GRÁFICA DE LOS EJERCICIOS

def defaultInterface (name,add):
  textUI = {
    "welcome": "- WELCOME -\n",
    "finish": "\n- PROGRAM FINISHED -\n",
    "inicio": "Bienvenido al programa 'Ciclos & Bucles' seleccione un ejercicio"+
    " que desea ejecutar.\n",
    "options": "Ejercicios\n\n\t[1] Números Naturales\n\t[2] Múltiplos de 5 y su Suma\n\t[3] Primeros números pares\n\t[4] Número de Edades pares\n\n-> ",  
    "input": "\n"+add+" -> ",
    "exit_option": "\n¿Desea seguir "+add+" para seguir aumentando la Lista?\n\n\t[Si]\n\t[No]\n\n-> ",
    "natural_n": "El siguiente ejercicio mostrará en una lista por pantalla todos los primeros números naturales según la cantidad que desee ingresar. ",
    "multiples_5": "El siguiente ejercicio mostrará en una lista por pantalla todos los primeros números múltiplos de 5 según la cantidad que desee ingresar, de igual manera su suma y respectivo promedio. ",
    "multiples_2": "El siguiente ejercicio mostrará en una lista por pantalla todos los primeros números múltiplos de 2 según la cantidad que se desee ingresar."
  }
  return textUI[str(name)]

def error (name,add,number):
  textUI = {    
    "error": "\n¡ERROR!: "+str(add)+" ["+str(number)+"]\n"
  }
  return textUI[str(name)]

def succes (name,add,info):
  textUI = {
    "succes": "¡SUCCES!: "+str(add)+" ["+str(info)+"]\n",
    "finish": "\n¡EN HORA BUENA! El resultado del ejercicio es el siguiente \n"+str(add)+" -> "+str(info)
  }
  return textUI[str(name)]