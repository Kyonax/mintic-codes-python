import json
import time
from tabulate import tabulate
from ..functions.logic import generateProductCode
from ..functions.gui import consoleGUI, clearGUI
from ..misc.employee import Employee
from ..misc.product import Product
from ..misc.employee_function import employee, employeeSelectParameter,employeeConfirmationData
from ..misc.product_function import product, productSelectParameter,productConfirmationData
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole


def insertEmployee(name,code,position,company,comission):
    employeeObj = Employee(name,code,position,company,comission)   
    clearGUI()
    print(consoleGUI("separador", "none", "none"))
    print(consoleGUI("employee-insert-select", "none", "none"))
    employeeDB = stateManagerRead(json, 'database/Employee_db.json')
    key_update = int(
        input(consoleGUI("employee-insert-options", "none", "none")))

    while key_update > 5 or key_update < 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        print(consoleGUI("error", "Ha ocurrido un error en la selección," +
                         " porfavor dígite alguna de las opciones que se encuentran en pantalla", "001"))
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI(
            "employee-insert-options", "none", "none")))
    
    iterator = 0     
    while employeeObj.iterator <= 3:
        employeeObj.iterator = iterator + 1                        
        data, dataType, iterator = employeeSelectParameter(key_update, employeeObj,employeeObj.comission)                           
        employeeObj.iterator = iterator
        if iterator == 31: break
        if employeeObj.name != "none" and employeeObj.code != "none" and employeeObj.position != "none" and employeeObj.company != None:
            iterator = employeeConfirmationData(employeeObj)
            if iterator > 4: break
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(
            input(consoleGUI("employee-insert-options", "none", "none")))
        if dataType == "name":            
            employeeObj.name = data
        elif dataType == "id":            
            employeeObj.code = data
        elif dataType == "position":            
            employeeObj.position = data
        elif dataType == "company":            
            employeeObj.company = data
        else:            
            employeeObj.comission = data

    if iterator != 31:
        test = employeeObj.code
        employeeObj = employee(employeeObj.name, employeeObj.code,
                            employeeObj.position, employeeObj.company, str(employeeObj.comission))
        employeeDB["employee"].append(employeeObj)
        stateManagerWrite(json, employeeDB, 'database/Employee_db.json')

        employeePrint = -1
        for employ in employeeDB["employee"]:     
            employeePrint = employeePrint+1
            if employ["id"] == test:                  
                break 

        clearGUI()     
        print(consoleGUI("result-data-insert","VENDEDOR/EMPLEADO","none"))    
        return print(tabulate([employeeDB["employee"][employeePrint]],headers='keys',tablefmt="psql"))
    return
    


def insertProduct(name,brand,color,size,price,iva,client,date,code):
    productObj = Product(name,brand,color,size,price,iva,client,date,code)   
    clearGUI()
    print(consoleGUI("separador", "none", "none"))
    print(consoleGUI("product-insert-select", "none", "none"))
    productDB = stateManagerRead(json, 'database/Product_db.json')
    key_update = int(
        input(consoleGUI("product-insert-options", "none", "none")))

    while key_update > 7 or key_update < 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        print(consoleGUI("error", "Ha ocurrido un error en la selección," +
                         " porfavor dígite alguna de las opciones que se encuentran en pantalla", "001"))
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI(
            "product-insert-options", "none", "none")))
    
    iterator = 0     
    while productObj.iterator <= 6:
        productObj.iterator = iterator + 1                        
        data, dataType, iterator = productSelectParameter(key_update, productObj,productObj.client,productObj.date)                           
        productObj.iterator = iterator        
        if iterator == 31: break
        if productObj.name != "none" and productObj.brand != "none" and productObj.color != "none" and productObj.size != "none" and productObj.price != 0 and productObj.iva != 0:
            iterator = productConfirmationData(productObj)
            if iterator > 7: 
                productObj.code = generateProductCode()
                break
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(
            input(consoleGUI("product-insert-options", "none", "none")))
        if dataType == "name":            
            productObj.name = data
        elif dataType == "brand":            
            productObj.brand = data
        elif dataType == "color":            
            productObj.color = data
        elif dataType == "size":            
            productObj.size = data
        elif dataType == "price":            
            productObj.price = data
        elif dataType == "iva":            
            productObj.iva = data       

    if iterator != 31:
        productCode = productObj.code
        productObj = product(productObj.name, productObj.brand,productObj.color,productObj.size,productObj.price,productObj.iva,productObj.client,productObj.date,productObj.code)
        productDB["product"].append(productObj)
        stateManagerWrite(json, productDB, 'database/Product_db.json')

        productPrint = -1
        for prod in productDB["product"]:     
            productPrint = productPrint+1
            print(prod)
            if prod["code"] == productCode:                  
                break 

        clearGUI()     
        print(consoleGUI("result-data-insert","PRODUCTO/BICICLETA","none"))    
        return print(tabulate([productDB["product"][productPrint]],headers='keys',tablefmt="psql"))
    return

def insertClient(name,code,product,total_price,amount_products):
    clientObj = Product(name, code, product, total_price, amount_products)   
    clearGUI()
    print(consoleGUI("separador", "none", "none"))
    print(consoleGUI("client-insert-select", "none", "none"))
    productDB = stateManagerRead(json, 'database/Product_db.json')
    key_update = int(
        input(consoleGUI("client-insert-options", "none", "none")))

    while key_update > 3 or key_update < 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        print(consoleGUI("error", "Ha ocurrido un error en la selección," +
                         " porfavor dígite alguna de las opciones que se encuentran en pantalla", "001"))
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI(
            "client-insert-options", "none", "none")))
    
    iterator = 0     
    while clientObj.iterator <= 2:
        clientObj.iterator = iterator + 1                        
        data, dataType, iterator = productSelectParameter(key_update, clientObj)                           
        clientObj.iterator = iterator        
        if iterator == 31: break
        if clientObj.name != "none" and clientObj.brand != "none" and clientObj.color != "none" and clientObj.size != "none" and clientObj.price != 0 and clientObj.iva != 0:
            iterator = productConfirmationData(clientObj)
            if iterator > 3: 
                clientObj.code = generateProductCode()
                clientObj.amount_products = len(productDB["product"])
                for productData in productDB:
                    clientObj.total_price = clientObj.total_price+productData["price"] 
                break
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(
            input(consoleGUI("client-insert-options", "none", "none")))
        if dataType == "name":            
            clientObj.name = data
        elif dataType == "product":            
            clientObj.product = data        

    if iterator != 31:
        productCode = productObj.code
        productObj = product(productObj.name, productObj.brand,productObj.color,productObj.size,productObj.price,productObj.iva,productObj.client,productObj.date,productObj.code)
        productDB["product"].append(productObj)
        stateManagerWrite(json, productDB, 'database/Product_db.json')

        productPrint = -1
        for prod in productDB["product"]:     
            productPrint = productPrint+1
            print(prod)
            if prod["code"] == productCode:                  
                break 

        clearGUI()     
        print(consoleGUI("result-data-insert","PRODUCTO/BICICLETA","none"))    
        return print(tabulate([productDB["product"][productPrint]],headers='keys',tablefmt="psql"))
    return    


def insertData(type, data):
    consoleGUI("separador", "none", "none")
    consoleGUI("insertar-init", "none", "none")
    key_data = input(consoleGUI("options-insert", "none", "none"))
    selectDataType(key_data)

# TIPO DE DATO NO EXISTENTE
def invalidDataType():
    raise print(consoleGUI(
        "error", "No se encuentra el dato digitado", "E-002"))
# FINALIZACIÓN DE LA ALERTA

# SELECCIÓN DE FUNCIONES (tipo de insercción)


def selectDataType(number):
    DataType = {
        1: employee,
    }
    selected = DataType.get(number, invalidDataType)
    return selected(number)
