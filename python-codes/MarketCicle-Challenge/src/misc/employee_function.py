import time
import json
from ..functions.gui import consoleGUI, clearGUI
from ..functions.logic import generateCode, createCode
from ..functions.stateManager import stateManagerRead


def employee(name, id, position, company, comission):
    employeeObj = {
        "name": name,
        "id": id,
        "position": position,
        "company": company,
        "comission": comission
    }
    return employeeObj


def employeeName(employeeObj,comission):    
    iterator = employeeObj.iterator
    validation = False
    data = "name"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))        
        name = input(consoleGUI("employee-insert-name", "none", "none"))        
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI("validation-data", "none", "none"))
        if key_validation.lower() == "si":
            validation = True            
            employeeObj.name = name                    
    return name, data, iterator


def employeeID(employeeObj,comission):    
    iterator = employeeObj.iterator
    validation = False
    data = "id"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_code = int(input(consoleGUI("employee-insert-id", "none", "none")))
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI(
            "validation-selection", "none", "none"))
        if key_validation.lower() == "si":
            if key_code == 1:
                code = generateCode()
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("employee-insert-id-show", code, "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                employeeObj.code = code
                time.sleep(3)
            elif key_code == 2:
                code = createCode()
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("employee-insert-id-show", code, "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                employeeObj.code = code
                time.sleep(3)            
    return code, data, iterator


def employeePosition(employeeObj,comission):
    iterator = employeeObj.iterator
    validation = False
    data = "position"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        position = input(consoleGUI("employee-insert-position","none","none"))
        clearGUI()
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))
        if key_validation.lower() == "si":
            validation = True
            employeeObj.position = "Vendedor"            
    return "Vendedor", data, iterator


def employeeCompany(employeeObj,comission):
    iterator = employeeObj.iterator
    validation = False
    data = "company"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        company = input(consoleGUI("employee-insert-company","none","none"))
        company = stateManagerRead(json,'database/Employee_db.json')
        clearGUI()
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))
        if key_validation.lower() == "si":
            validation = True
            employeeObj.company = company["company"]            
    return company["company"]["name"], data, iterator



def employeeComission(employeeObj,comission):
    employeeObj.comission = employeeObj.comission + comission
    return str(employeeObj.comission)

# TIPO DE DATO NO EXISTENTE


def invalidParameter():
    raise print(consoleGUI(
        "error", "No se encuentra el parametro solicitado", "E-002"))
# FINALIZACIÓN DE LA ALERTA


def overWriteData(number,employeeObj):                 
    key_overwrite = "si"
    iterator = employeeObj.iterator      
    if number == 1 and employeeObj.name != "none":
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+employeeObj.name,"none"))        
        iterator = employeeObj.iterator - 1
        employeeObj.iterator = iterator
    elif number == 2 and employeeObj.code !=  "none":
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+employeeObj.name+" código "+employeeObj.code,"none"))        
        iterator = employeeObj.iterator - 1
        employeeObj.iterator = iterator
    elif number == 3 and employeeObj.position != "none":
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+employeeObj.name+" código "+employeeObj.code+" Cargo "+employeeObj.position,"none"))        
        iterator = employeeObj.iterator - 1
        employeeObj.iterator = iterator
    elif number == 4 and employeeObj.company != None:
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+employeeObj.name+" código "+employeeObj.code+" Cargo "+employeeObj.position+" de la Compañia "+employeeObj.company,"none"))
        iterator = employeeObj.iterator - 1
        employeeObj.iterator = iterator    
    return key_overwrite,iterator   
    
def exitFunction(employeeObj,comission):
    iterator = 31
    return "none", "none", iterator

def employeeConfirmationData (employeeObj):
    clearGUI()
    iterator = employeeObj.iterator
    key_confirmation = input(consoleGUI("confirmation-data","Vendedor/Empleado","none"))
    if key_confirmation == 1:        
        iterator = iterator-1        
    else:
        iterator = iterator+2
    return iterator, key_confirmation


def employeeSelectParameter(number,employeeObj,comission):  
    key_overwrite, employeeObj.iterator = overWriteData(number,employeeObj)                                 
    if key_overwrite.lower() == "no":
        return "none","none",employeeObj.iterator

    Parameter = {
        1: employeeName,
        2: employeeID,
        3: employeePosition,
        4: employeeCompany,
        5: exitFunction,
        6: employeeComission
    }      
     
    selected = Parameter.get(number, invalidParameter)    
    return selected(employeeObj,comission)

    
