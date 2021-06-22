import json
import time
from tabulate import tabulate
from ..functions.gui import consoleGUI, clearGUI
from ..misc.employee import Employee
from ..misc.employee_function import employee, employeeSelectParameter,employeeConfirmationData
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

    test = employeeObj.code

    employeeObj = employee(employeeObj.name, employeeObj.code,
                           employeeObj.position, employeeObj.company, str(employeeObj.comission))
    employeeDB["employee"].append(employeeObj)
    stateManagerWrite(json, employeeDB, 'database/Employee_db.json')

    employeePrint = -1
    for employ in employeeDB["employee"]:     
        print("1: "+employ["id"]+" 2: "+test+"Posi: "+str(employeePrint))             
        time.sleep(0.5)      
        employeePrint = employeePrint+1
        if employ["id"] == test:      
            print("POSITIOn: "+str(employeePrint))     
            time.sleep(4) 
            break 

    clearGUI()
    print(consoleGUI("separador","none","none"))        
    return print(tabulate(employeeDB["employee"][employeePrint],headers='keys',tablefmt="psql"))
    


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
