import os
#INTERFAZ GRÁFICA DEL USUARIO
def graphicalConsoleUI (name,add):  
  textUI = {
    "inicio": "- MARKET CICLE - VENTAS \nBienvenido/Bienvenida al programa de 'Ventas de Market Cicle' Seleccione alguna de las siguiente opciones"+
    " para proceder a la ejecución del programa.\n",
    "separador": "="*80+"\n",
    "insertar-init": "- MARKET CICLE - REGISTRO DE USUARIOS & PRODUCTOS\nSeleccione el nuevo dato que desea Ingresar, para proceder con el Registro:\n",
    "options-insert": "Nuevo Dato - \n[1] Vendedor/Empleado.\n[2] Producto.\n[3] Cliente\n\n-> ",        
    "employee-insert-select": "Para ingresar un nuevo Vendedor/Empleado seleccione las opciones a continuación.\n",
    "employee-insert-options": "Datos a Ingresar del nuevo Vendedor/Empleado\n[1] Nombre del Vendedor/Empleado.\n[2] Código del Vendedor/Empleado.\n[3] Cargo que desempeña.\n[4] Compañia a la que pertenece.\n\n-> ",
    "employee-insert-name": "Dígite el Nombre Completo del nuevo Vendedor/Empleado de la Empresa.\n\n-> ",
    "employee-insert-id": "Código de Vendedor/Empleado seleccione una de las dos Opciones.\n[1] Generar Código\n[2] Escribir Código\n\n-> ",
    "validation-data": "¿Está seguro/segura que desea guardar los cambios? Una vez se guarden los Datos\nEl programa lo llevará a la anterior Interfaz.\n\n[Si] - [No] -> ",
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
    "error": "¡ERROR!: "+add+" ["+number+"]\n"
  }
  return textUI[str(name)]

def succesGUI (name,add, number):
  textUI = {
    "succes": "¡SUCCES!: "+add+" ["+number+"]\n"
  }
  return textUI[str(name)]

def clearGUI ():
  return os.system('cls')

def consoleGUI (name,add,number):
    if number != "none":
        if name == "error":
            return errorGUI(name,add,number)
        else:
            return succesGUI(name,add,number)
    else:
        return graphicalConsoleUI(name,add)    
    