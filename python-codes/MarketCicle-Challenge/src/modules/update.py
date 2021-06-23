import json
import time
from tabulate import tabulate
from ..functions.gui import consoleGUI, clearGUI
from .insert import insertEmployee, insertProduct, insertClient
from .consult import consultEmployee, consultProduct, consultClient
from .remove import removeEmployee, removeProduct, removeClient
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole

def updateEmployee(codeEmployee):       
    employeeDB = stateManagerRead(json,"database/Employee_db.json")

    iteratorObj = 0
    employeeObj = None
    for employee in employeeDB["employee"]:
        if employee["id"] == codeEmployee:
            employeeObj = employee
            break
        iteratorObj = iteratorObj+1

    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("update-preview","Vendedor/Empleado","none"))
    consultEmployee(codeEmployee)
    clearGUI()    
    removeEmployee(codeEmployee)
    insertEmployee(employeeObj["name"], employeeObj["id"], employeeObj["position"], employeeObj["company"], employeeObj["comission"])
    return

def updateProduct(codeProduct):
    productDB = stateManagerRead(json,"database/Product_db.json")

    iteratorObj = 0
    productObj = None
    for product in productDB["product"]:
        if product["code"] == codeProduct:
            productObj = product
            break
        iteratorObj = iteratorObj+1

    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("update-preview","Vendedor/Empleado","none"))
    consultProduct(codeProduct)
    clearGUI()    
    removeProduct(codeProduct)
    insertProduct(productObj["name"], productObj["brand"], productObj["color"], productObj["size"], productObj["price"], productObj["iva"], productObj["client"],productObj["date"], productObj["code"])
    return

def updateClient(codeClient):
    clientDB = stateManagerRead(json,"database/Client_db.json")

    iteratorObj = 0
    clientObj = None
    for client in clientDB["client"]:
        if client["code"] == codeClient:
            clientObj = client
            break
        iteratorObj = iteratorObj+1

    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("update-preview","Vendedor/Empleado","none"))
    consultClient(codeClient)
    clearGUI()    
    removeClient(codeClient)
    insertClient(clientObj["name"], clientObj["code"], clientObj["product"], clientObj["total_price"], clientObj["amount_products"])
    return
