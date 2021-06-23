import os
#INTERFAZ GRÁFICA DEL USUARIO
def graphicalConsoleUI (name,add):  
  textUI = {
    "inicio": "- MARKET CICLE - VENTAS \nBienvenido/Bienvenida al programa de 'Ventas de Market Cicle' Este programa es el gestor principal de las ventas "+
    "\nQue realiza Market-Cicle, con este programa puedes Registrar, Consultar, Listar, Remover y Vender productos de Market Cicle.\n\nContinuar? -> ",
    "inicio-2":"- RECOMENDACIÓN -\nEl programa cuenta con 2 apartados, que puedes elegir para empezar a utilizar el programa,\n"+
    " se te recomienda que leas atentamente y que navegues por el menú para que aprendas a usar el programa.\n\nContinuar? -> ",    
    "inicio-options":"- TIENDA & CONFIGURACIÓN -\nSelecciona alguna de las opciones que encuentras abajo para comenzar a navegar.\n\n[1] Tienda\n[2] Configuración\n[3] Salir del Programa\n\n-> ",
    "tienda": "- VENTAS & PRODUCTOS -\nEn este menu podrás encontrar el apartado de ventas y productos, aquí podrás comenzar a vender\n"+
    " productos en nombre de Market Cicle y de igual manera Crearlos, Editarlos y Consultarlos por si lo necesitas.\n\n[1] Vender\n[2] Productos Market Cicle\n[3] Retroceder\n\n-> ",
    "config": "- EMPLEADOS & REPORTES -\nEn este menu podrás encontrar el apartado administrativo, aquí podrás configurar a los nuevos Empleados\n"+
    " y realizar reportes de las estadísticas de las ventas.\n\n[1] Empleados\n[2] Reportes\n[3] Retroceder\n\n-> ",
    "sell": "- VENDER A NUEVO CLIENTE -\nEn este menu podrás encontrar el apartado administrativo, aquí podrás configurar a los nuevos Empleados\n"+
    " y realizar reportes de las estadísticas de las ventas.\n\n[1] Empleados\n[2] Reportes\n[3] Retroceder\n\n-> ",
    "separador": "="*80+"\n",
    "insertar-init": "- MARKET CICLE - REGISTRO DE USUARIOS & PRODUCTOS\nSeleccione el nuevo dato que desea Ingresar, para proceder con el Registro:\n",
    "options-insert": "Nuevo Dato - \n[1] Vendedor/Empleado.\n[2] Producto.\n[3] Cliente\n\n-> ",        
    "employee-insert-select": "Para Ingresar o Actualizar un Vendedor/Empleado seleccione las opciones a continuación.\n",
    "employee-insert-options": "Datos a Ingresar del Vendedor/Empleado\n[1] Nombre del Vendedor/Empleado.\n[2] Código del Vendedor/Empleado.\n[3] Cargo que desempeña.\n[4] Compañia a la que pertenece.\n[5] Salir\n\n-> ",
    "employee-insert-name": "Dígite el Nombre Completo del Vendedor/Empleado de la Empresa.\n\n-> ",
    "employee-insert-id": "Código de Vendedor/Empleado seleccione una de las Opciones.\n[1] Generar Código\n[2] Escribir Código\n\n-> ",
    "employee-insert-id-show": "Código generado por procesos: "+add+"\n",
    "employee-insert-id-create": "Para crear el código de Vendedor/Empleado se necesita digitar una ID de 5 Carácteres, \n"+
    "Luego el programa le añadirá el separador '*' y el identificador al inicio y al final del código.\n\n"+
    "Proceda a ingresar los 5 Carácteres\n\n-> ",
    "employee-insert-position": "Cargo de Vendedor/Empleado seleccione una de las Opciones.\n[1] Vendedor\n\n-> ",
    "employee-insert-company": "Empresa a la que se encuentra Afiliado el Empleado.\n[1] Market Cicle\n\n-> ",
    "product-insert-select": "Para ingresar o Actualizar un  Producto/Bicicleta seleccione las opciones a continuación.\n",
    "product-insert-options": "Datos a Ingresar del Producto\n[1] Nombre del Producto.\n[2] Marca del Producto.\n[3] Color del Producto.\n[4] Tamaño del Producto.\n[5] Precio del Producto.\n[6] IVA del Producto.\n[7] Salir\n\n-> ",
    "product-insert-name": "Dígite el Nombre Completo del Producto que se agregará a la Empresa.\n\n-> ",
    "product-insert-id": "Marca del Producto/Bicicleta seleccione una de las Opciones.\n[1] Specialized\n[2] Treck\n[3] BMC\n\n-> ",
    "product-insert-id-show": "Dato seleccionado por el usuario: "+add+"\n",
    "product-insert-color": "Color del Producto/Bicicleta seleccione una de las Opciones.\n[1] Rojo\n[2] Negro\n[3] Rojo-Negro\n\n-> ",
    "product-insert-size": "Tamaño del Producto/Bicicleta seleccione una de las Opciones.\n[1] S\n[2] M\n[3] L\n[4] XL\n\n-> ",
    "product-insert-price": "Ingrese el Valor del Producto/Bicicleta sin puntos ni comas.\n\n-> ",
    "product-insert-iva": "Ingrese el IVA del Producto/Bicicleta sin puntos ni comas.\n\n-> ",
    "client-insert-name": "Dígite el Nombre Completo del Cliente que Realizará una compra.\n\n-> ",    
    "client-insert-product": "Cargo de Vendedor/Empleado seleccione el Producto a Vender.\n"+add+"\n\n-> ",
    "client-insert-select": "Para ingresar un nuevo Cliente y proceder a una compra seleccione las opciones a continuación.\n",
    "client-insert-options": "Datos a Ingresar del Cliente y Nueva Venta\n[1] Nombre del Cliente.\n[2] Seleccionar Productos.\n[3] Salir\n\n-> ",
    "confirmation-data": "Ha completado todos los datos para Ingresar al nuevo "+add+"\n¿Desea Guardar los Cambios?\n[1] No, Deseo actualizar algunos Datos.\n[2] Sí, Deseo Guardar los Datos\n\n-> ",
    "result-data-insert":"ESTOS SON LOS DATOS QUE HA INGRESADO EN LA BASE DE DATOS DE "+add,
    "overwrite-data": "¿Está seguro/segura que desea sobreescribir los datos previamente registrados del "+add+"?\n\n[Si] - [No] -> ",
    "validation-data": "¿Está seguro/segura que desea guardar los cambios? Una vez se guarden los Datos\nEl programa los registrará en la Base de Datos.\n\n[Si] - [No] -> ",
    "validation-store": "¿Desea Seguir realizando Ventas a este Usuario? Puede agregar las Ventas que desee\nSiempre y cuando cuente con el Stock necesario.\n\n[Si] - [No] -> ",
    "validation-selection": "¿Está seguro/segura que desea proceder con esta opción? Una vez se guarden los Datos\nLa desición grabará y registrará los Datos.\n\n[Si] - [No] -> ",
    "update-data": "Para proceder a realizar la correcta actualización de datos de los "+add+" digite el código que corresponde al Objeto.\n",    
    "update-preview": "Está observando el "+add+" al que le realizará la Actualización.\n",    
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
    
