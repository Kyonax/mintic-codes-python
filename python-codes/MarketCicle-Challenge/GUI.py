#INTERFAZ GRÁFICA DEL USUARIO

def graphicalConsoleUI (name,add):  
  textUI = {
    "inicio": "- MARKET CICLE VENTAS -\nBienvenido/Bienvenida al programa de 'Ventas de Market Cicle' Seleccione alguna de las siguiente opciones"+
    " para proceder a la ejecución del programa.\n",
    "separador": "="*10,
    "welcome": "- WELCOME -\n",
    "options": "Ejercicios - \n[1] Número Positivo o Negativo\n[2] Número Par o Impar\n[3] Número Múltiplo de 3 y 5\n[4] ¿Carácter es Vocal?\n\n-> ",        
    "exercise_description": "Este programa define "+str(add)+".",
    "in_data": "Porfavor digite "+str(add)+": ",    
    "number_positive": "EL NÚMERO "+str(add)+" ES POSITIVO.\n\n",
    "number_negative": f"EL NÚMERO "+str(add)+" ES NEGATIVO.\n\n",
    "number_par": "EL NÚMERO "+str(add)+" ES PAR.\n\n",
    "number_impar": f"EL NÚMERO "+str(add)+" ES IMPAR.\n\n",
    "number_multiple3": "EL NÚMERO "+str(add)+" ES MÚLTIPLO DE 3 Y 5.\n\n",
    "number_nomultiple3": f"EL NÚMERO "+str(add)+" NO ES MÚLTIPLO DE 3 Y 5.\n\n",
    "char_vocal": "EL CÁRACTER "+str(add)+" ES UNA VOCAL.\n\n",
    "char_novocal": f"EL CARÁCTER "+str(add)+" NO ES UNA VOCAL.\n\n"
  }
  return textUI[str(name)]    

def errorGUI (name,add,number):
  textUI = {    
    "error": "\n¡ERROR!: "+add+" ["+number+"]\n"
  }
  return textUI[str(name)]

def succesGUI (name,add, number):
  textUI = {
    "succes": "\n¡SUCCES!: "+add+" ["+number+"]\n"
  }
  return textUI[str(name)]

def consoleGUI (name,add,number):
    if number != "none":
        if name == "error":
            return print(errorGUI(name,add,number))
        else:
            return print(succesGUI(name,add,number))
    else:
        return print(graphicalConsoleUI(name,add))
    
