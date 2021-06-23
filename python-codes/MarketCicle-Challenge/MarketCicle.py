import time
import json
from src.misc.employee import Employee
from src.misc.employee_function import employee
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
        if key_init_option == 3:
            validation_option_init = True
            break        


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
    productDB = stateManagerRead(json, 'database/Product_db.json')
    clientDB = stateManagerRead(json, 'database/Client_db.json')
    employeeDB = stateManagerRead(json, 'database/Employee_db.json')
    key_code_employee = input(consoleGUI("employee_code_obj","Vendedor/Empleado","none"))
    for employee in employeeDB["employee"]:
        if employee["id"] != key_code_employee:
            clearGUI()
            print(consoleGUI("separador","none","none"))
            print(consoleGUI("error","El código Ingresado no pertenece a ningún Vendedor/Empleado, si desea registrase dirijase a Registro de Vendedores.","0012"))
            input("\n\nContinuar? -> ")
            start()
        else:
            clearGUI()
            print(consoleGUI("separador","none","none"))
            print(consoleGUI("succes","En hora buena!!! Se ha detectado al respectivo Vendedor/Empleado, porfavor proceda con la Venta o Actualización.","003"))
            input("\n\nContinuar? -> ")
            break                

    clearGUI()
    print(consoleGUI("separador","none","none"))
    key_client_options = int(input(consoleGUI("client-options","none","none")))
    clearGUI()
    print(consoleGUI("separador","none","none"))
    clientObj = selectOption(key_client_options,"client")      
    if key_client_options == 1:
        codeProductObj = clientObj("none","none",[],0,0)
        comissionEmployee = 0
        
        for products in productDB["product"]:
            if products["code"] == codeProductObj:                                
                comissionEmployee = float(products["price"])+((float(products["iva"])*100)/float(products["price"]))                
        
        if comissionEmployee >= 200000 and comissionEmployee < 800000:
            comissionEmployee = comissionEmployee*0.05
        if comissionEmployee >= 800000 and comissionEmployee < 1500000:
            comissionEmployee = comissionEmployee*0.1
        if comissionEmployee >= 1500000:
            comissionEmployee = comissionEmployee*0.15

        iteratorProduct = 0
        for employees in employeeDB["employee"]:
            if employees["id"] == key_code_employee:                                   
                employeeDB["employee"][iteratorProduct]["comission"] = comissionEmployee                                
                stateManagerWrite(json,employeeDB,'database/Employee_db.json') 
            iteratorProduct = iteratorProduct+1            

    elif key_client_options == 2:
        clientObj()
    elif key_client_options == 3 or key_client_options == 4 or key_client_options == 5:
        clearGUI()
        key_code_client = input(consoleGUI("employee_code_obj","Cliente","none"))
        clientObj(key_code_client)
    elif key_client_options == 6:
        start()
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
        3: client,
        4: exitMenu
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
graph()
start()