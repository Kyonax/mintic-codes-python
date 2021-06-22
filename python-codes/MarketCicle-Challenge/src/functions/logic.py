import json
import time
from ..functions.gui import consoleGUI, clearGUI
from ..functions.stateManager import stateManagerRead


def generateCode ():
    employeeDB = stateManagerRead(json,'database/Employee_db.json')
    companyName = str(employeeDB["company"]["name"])
    employeeLength = len(employeeDB["employee"])
    firstCode = companyName[0]+str(employeeLength)

    if employeeLength < 10:
        secondCode = "000"+str(employeeLength)
    elif employeeLength >= 10 and employeeLength < 100:
        secondCode = "00"+str(employeeLength)+"0"
    elif employeeLength >= 100 and employeeLength < 1000:
        secondCode = "0"+str(employeeLength)+"00"
    elif employeeLength >= 1000 and employeeLength < 10000:
        secondCode = str(employeeLength)+"000"

    finalCode = firstCode+"*"+secondCode+companyName[0]    
    return finalCode

def createCode ():
    employeeDB = stateManagerRead(json,'database/Employee_db.json')
    companyName = str(employeeDB["company"]["name"])

    clearGUI()
    print(consoleGUI("separador","none","none"))
    inputCode = input(consoleGUI("employee-insert-id-create","none","none"))

    for char in inputCode:                        
        disallowed_chars = "@+=&"
        for character in disallowed_chars:
	        inputCode = inputCode.replace(character, "C")
        if len(inputCode) > 5:               
            inputCode = inputCode[:-1]                
    
    inputCode = inputCode.upper()    
    firstCode = companyName[0]+inputCode[0]        
    inputCode = inputCode[1:]    
    finalCode = firstCode+"*"+inputCode+companyName[0]        
    return finalCode

