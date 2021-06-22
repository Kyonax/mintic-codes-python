import json
import time
from tabulate import tabulate
from ..functions.gui import consoleGUI, clearGUI
from ..misc.employee import Employee
from ..misc.employee_function import employee, employeeSelectParameter
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
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(
            input(consoleGUI("employee-insert-options", "none", "none")))
        if dataType == "name":            
            employeeObj.name = data
        elif dataType == "id":            
            employeeObj.id = data
        elif dataType == "position":            
            employeeObj.position = data
        elif dataType == "company":            
            employeeObj.company = data
        else:            
            employeeObj.comission = data

    employeeObj = employee(employeeObj.name, employeeObj.id,
                           employeeObj.position, employeeObj.company, employeeObj.comission)
    employeeDB["employee"].append(employeeObj)
    stateManagerWrite(json, employeeDB, 'database/Employee_db.json')
    clearGUI()
    print(consoleGUI("separador","none","none"))
    
    return print(tabulate(employeeDB["employee"],headers='keys'))
    


def insertProduct():
    return


def insertClient():

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
