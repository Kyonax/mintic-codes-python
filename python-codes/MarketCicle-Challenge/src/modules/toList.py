from tabulate import tabulate
from ..misc.employee import Employee
from ..misc.product import Product
from ..misc.client import Client
import time
import json
from ..functions.gui import consoleGUI, clearGUI
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole

def toListEmployees():
    employeeDB = stateManagerRead(json,"database/Employee_db.json")
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado la Lista de Vendedores/Empleados con éxito.","001"))
    print(tabulate(employeeDB["employee"],headers='keys',tablefmt="psql"))
    time.sleep(6)
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se han Mostrado los Vendedores/Empleados con éxito.","001"))
    time.sleep(4)
    return

def toListProducts():
    productDB = stateManagerRead(json,"database/Product_db.json")
    clientDB = stateManagerRead(json,"database/Client_db.json")
    clearGUI()
    productNameProduct = []
    iteratorExport = 0
    for productData in productDB["product"]:  
        for client in productData["client"]:            
            productNameProduct.append("Cliente: "+str(client["name"])+" - ID: "+str(client["code"]))
            productData["client"] = productNameProduct
        iteratorExport = iteratorExport +1        

    productPrint = -1
    for cli in productDB["product"]:     
        productPrint = productPrint+1                    
    

    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado la Lista de Productos con éxito.","001"))
    print(tabulate(productDB["product"],headers='keys',tablefmt="psql"))
    key_continue = input("\n\nContinuar? -> ")
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se hab Mostrado los Productos con éxito.","001"))
    time.sleep(4)
    return

def toListClients():
    clientDB = stateManagerRead(json,"database/Client_db.json")
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado la Lista de Clientes con éxito.","001"))
    print(tabulate(clientDB["client"],headers='keys',tablefmt="psql"))
    time.sleep(6)
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado los Mimebtros con éxito.","001"))
    time.sleep(4)
    return