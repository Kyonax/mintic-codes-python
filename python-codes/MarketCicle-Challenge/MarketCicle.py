import time
from src.functions.gui import consoleGUI, clearGUI
from src.modules.insert import insertEmployee, insertProduct, insertClient
from src.modules.remove import removeEmployee, removeProduct, removeClient
from src.modules.toList import toListEmployees, toListProducts, toListClients
from src.modules.consult import consultEmployee, consultProduct, consultClient
from src.modules.update import updateEmployee, updateProduct, updateClient

def start():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    init = input(consoleGUI("inicio","none","none"))
    clearGUI()
    print(consoleGUI("separador","none","none"))
    init2 = input(consoleGUI("inicio-2","none","none"))
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_init_option = input(consoleGUI("inicio-options","none","none"))
    validation_option_init = False
    while validation_option_init == False:
        if key_init_option == 1:
            store()
        elif key_init_option == 2:
            config()
        elif key_init_option == 3:
            break
        else:
            clearGUI()
            print(consoleGUI("separador","none","none"))
            print(consoleGUI("error","Por el momento sólo se encuentran habilitadas esas 2 opciones, selecciona alguna de ellas!!","006"))
            time.sleep(3)


def store():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_store_option = input(consoleGUI("tienda","none", "none"))
    validation_option_store = False
    while validation_option_store == False:
        if key_store_option == 1:
            sell()
        elif key_store_option == 2:
            products()
        elif key_store_option == 3:
            break
        else:
            clearGUI()
            print(consoleGUI("separador","none","none"))
            print(consoleGUI("error","Por el momento sólo se encuentran habilitadas esas 2 opciones, selecciona alguna de ellas!!","006"))
            time.sleep(3)
    return 

def config():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_store_option = input(consoleGUI("config","none", "none"))
    validation_option_config = False
    while validation_option_config == False:
        if key_store_option == 1:
            sell()
        elif key_store_option == 2:
            products()
        elif key_store_option == 3:
            break
        else:
            clearGUI()
            print(consoleGUI("separador","none","none"))
            print(consoleGUI("error","Por el momento sólo se encuentran habilitadas esas 2 opciones, selecciona alguna de ellas!!","006"))
            time.sleep(3)
    return 

def sell():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_sell_option = input(consoleGUI("config","none", "none"))
    validation_option_config = False
    while validation_option_config == False:
        if key_sell_option == 1:
            sell()
        elif key_sell_option == 2:
            products()
        elif key_sell_option == 3:
            break
        else:
            clearGUI()
            print(consoleGUI("separador","none","none"))
            print(consoleGUI("error","Por el momento sólo se encuentran habilitadas esas 2 opciones, selecciona alguna de ellas!!","006"))
            time.sleep(3)
    return

def products():
    return

def employee():
    return

def reports():
    return

key_option = int(input("OPCIONES\n[1] Employee Insert\n[2] Product Insert\n[3] Client Insert\n[4] Eliminar Cliente\n\n-> "))

if key_option == 1:
    insertEmployee("none","none","none",None,0)    
elif key_option == 2:
    insertProduct("none","none","none","none",0,0,[],"none","none")
elif key_option == 3:
    insertClient("none","none",[],0,0)
elif key_option == 4:
    removeClient("M2*0002M")
elif key_option == 5:
    updateClient("M2*0002M")
else:
    print("no entra")