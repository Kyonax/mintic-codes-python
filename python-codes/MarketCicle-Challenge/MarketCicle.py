import time
import json
from src.functions.gui import consoleGUI, clearGUI
from src.modules.insert import insertEmployee, insertProduct, insertClient
from src.modules.remove import removeEmployee, removeProduct, removeClient
from src.modules.toList import toListEmployees, toListProducts, toListClients
from src.modules.consult import consultEmployee, consultProduct, consultClient
from src.modules.update import updateEmployee, updateProduct, updateClient
from src.functions.stateManager import stateManagerRead, stateManagerWrite


def welcomeMessage():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    init = input(consoleGUI("inicio","none","none"))
    clearGUI()
    print(consoleGUI("separador","none","none"))
    init2 = input(consoleGUI("inicio-2","none","none"))
    return

def start():    
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_init_option = int(input(consoleGUI("inicio-options","none","none")))
    validation_option_init = False
    while validation_option_init == False:        
        clearGUI()
        print(consoleGUI("separador","none","none"))
        selectPropertie(key_init_option)           


def employee():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_employee_options = int(input(consoleGUI("employee-options","none","none")))
    clearGUI()
    print(consoleGUI("separador","none","none"))
    employeeObj = selectOption(key_employee_options,"employee")      
    if key_employee_options == 1:
        employeeObj("none","none","none",None,0)
    elif key_employee_options == 2:
        employeeObj()
    elif key_employee_options == 3 or key_employee_options == 4 or key_employee_options == 5:
        clearGUI()
        key_code_employee = input(consoleGUI("employee_code_obj","Vendedor/Empleado","none"))
        employeeObj(key_code_employee)
    elif key_employee_options == 6:
        start()
    return

def product():
    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_product_options = int(input(consoleGUI("product-options","none","none")))
    clearGUI()
    print(consoleGUI("separador","none","none"))
    productObj = selectOption(key_product_options,"product")      
    if key_product_options == 1:
        productObj("none","none","none","none",0,0,[],"none","none")
    elif key_product_options == 2:
        productObj()
    elif key_product_options == 3 or key_product_options == 4 or key_product_options == 5:
        clearGUI()
        key_code_product = input(consoleGUI("employee_code_obj","Producto/Bicicleta","none"))
        productObj(key_code_product)
    elif key_product_options == 6:
        start()
    return

def client():
    return

def exitMenu():
    return
    
def invalidParameter():
    return print(consoleGUI(
        "error", "La opción solicitada no se encuentra, disponible", "E-002"))

def selectPropertie(number):
    Parameter = {
        1: employee,
        2: product,
        3: client
    }
    selected = Parameter.get(number,invalidParameter)
    return selected()

def selectOption(number,obj):
    if obj == "employee":
        Parameter = {
            1: insertEmployee,
            2: toListEmployees,
            3: consultEmployee,
            4: updateEmployee,
            5: removeEmployee,
            6: exitMenu
        } 
    elif obj == "product":
        Parameter = {
            1: insertProduct,
            2: toListProducts,
            3: consultProduct,
            4: updateProduct,
            5: removeProduct,
            6: exitMenu
        }
    elif obj == "client":
        Parameter = {
            1: insertClient,
            2: toListClients,
            3: consultClient,
            4: updateClient,
            5: removeClient,
            6: exitMenu
        }
    selected = Parameter.get(number,invalidParameter)
    return selected

welcomeMessage()
start()