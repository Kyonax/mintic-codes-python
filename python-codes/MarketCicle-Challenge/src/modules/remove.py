import json
from ..functions.gui import consoleGUI, clearGUI
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole


def removeEmployee(employeeCode):    
    employeeDB = stateManagerRead(json,"database/Employee_db.json")
    iterator = 0
    for employee in employeeDB["employee"]:        
        if employee["id"] == employeeCode:
            del employeeDB["employee"][iterator]
        iterator = iterator +1
    stateManagerWrite(json, employeeDB, 'database/Employee_db.json')
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Eliminado al Vendedor/Empleado con éxito.","001"))
    return


def removeProduct(productCode):
    productDB = stateManagerRead(json,"database/Product_db.json")
    iterator = 0
    for product in productDB["product"]:
        if product["code"] == productCode:
            del productDB["product"][iterator]
        iterator = iterator +1
    stateManagerWrite(json, productDB, 'database/Product_db.json')
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Eliminado el Producto/Bicicleta con éxito.","002"))
    return


def removeClient(clientCode):
    clientDB = stateManagerRead(json,"database/Client_db.json")
    iterator = 0
    for client in clientDB["client"]:
        if client["code"] == clientCode:
            del clientDB["client"][iterator]
        iterator = iterator +1
    stateManagerWrite(json, clientDB, 'database/Client_db.json')
    clearGUI()
    print(consoleGUI("separador","none","none"))
    print(consoleGUI("succes","Se ha Eliminado el Cliente con éxito.","003"))
    return
