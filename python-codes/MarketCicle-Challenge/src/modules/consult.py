from tabulate import tabulate
from ..misc.employee import Employee
from ..misc.product import Product
from ..misc.client import Client
import time
import json
from ..functions.gui import consoleGUI, clearGUI
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole

def consultEmployee(codeEmployee):
    employeeDB = stateManagerRead(json,"database/Employee_db.json")

    iteratorObj = 0
    for employee in employeeDB["employee"]:
        if employee["id"] == codeEmployee:
            break
        iteratorObj = iteratorObj+1

    
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado la información del Usuario de código ["+codeEmployee+"]","001"))
    print(tabulate([employeeDB["employee"][iteratorObj]],headers='keys',tablefmt="psql"))
    key_continue = input("\n\nContinuar? -> ")
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se han Mostrado los Vendedores/Empleados con éxito.","001"))
    time.sleep(4)
    return

def consultProduct(codeProduct):
    productDB = stateManagerRead(json,"database/Product_db.json")    
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
    
    iteratorObj = 0
    for employee in productDB["product"]:
        if employee["code"] == codeProduct:
            break
        iteratorObj = iteratorObj+1

    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado la Información del Producto de código "+codeProduct,"001"))
    print(tabulate([productDB["product"][iteratorObj]],headers='keys',tablefmt="psql"))
    key_continue = input("\n\nContinuar? -> ")
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se hab Mostrado los Productos con éxito.","001"))
    time.sleep(4)
    return

def consultClient(codeClient):
    clientDB = stateManagerRead(json,"database/Client_db.json")
    clearGUI()

    productNameProduct = []
    iteratorExport = 0
    for productData in clientDB["client"]:  
        for client in productData["product"]:            
            productNameProduct.append("Producto: "+str(client["name"])+" - Código: "+str(client["code"]))
            productData["product"] = productNameProduct
        iteratorExport = iteratorExport +1        

    productPrint = -1
    for cli in clientDB["client"]:     
        productPrint = productPrint+1

    iteratorObj = 0
    for employee in clientDB["client"]:
        if employee["code"] == codeClient:
            break
        iteratorObj = iteratorObj+1

    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado la Lista de Clientes con éxito.","001"))
    print(tabulate([clientDB["client"][iteratorObj]],headers='keys',tablefmt="psql"))
    key_continue = input("\n\nContinuar? -> ")
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Mostrado los Mimebtros con éxito.","001"))
    time.sleep(4)
    return