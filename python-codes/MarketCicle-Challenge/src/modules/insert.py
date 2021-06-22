import json
from ..functions.gui import consoleGUI, clearGUI
from ..misc.employee import employee, employeeSelectParameter
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole


def insertEmployee():
    clearGUI()
    print(consoleGUI("separador", "none", "none"))
    print(consoleGUI("employee-insert-select", "none", "none"))
    employeeDB = stateManagerRead(json, 'database/Employee_db.json')
    key_update = int(input(consoleGUI("employee-insert-options", "none", "none")))

    while key_update > 4 or key_update < 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        print(consoleGUI("error", "Ha ocurrido un error en la selección," +
                   " porfavor dígite alguna de las opciones que se encuentran en pantalla", "001"))
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI(
            "employee-insert-options", "none", "none")))

    iterator = 0
    while iterator <= 3:
        iterator = iterator + 1
        data, dataType = employeeSelectParameter(key_update)
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI("employee-insert-options", "none", "none")))

        if dataType == "name":
            employeeName = data
        elif dataType == "id":
            employeeID = data
        elif dataType == "position":
            employeePosition = data
        elif dataType == "company":
            employeeCompany = data
        else:
            employeeComission = data        

    employeeObj = employee(employeeName,employeeID,employeePosition,employeeCompany,employeeComission)
    employeeDB["employee"].append(employeeObj)
    stateManagerWrite(json,employeeDB,'database/Employee_db.json')
    return


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
