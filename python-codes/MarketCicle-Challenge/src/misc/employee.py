from ..functions.gui import consoleGUI, clearGUI

def employee(name,id,position,company,comission):               
    employeeObj = {
       "name": name,
       "id": id,
       "position": position,
       "company": company,
       "comission": comission
    }        
    return employeeObj

def employeeName():    
    validation = False
    data = "name"    
    while validation == False:  
        clearGUI()        
        print(consoleGUI("separador","none","none"))
        name = input(consoleGUI("employee-insert-name","none","none"))     
        clearGUI()   
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))        
        if key_validation.lower() == "si":                        
            validation = True                                      
    return name, data        

def employeeID():
    validation = False
    data = "id"    
    while validation == False:  
        clearGUI()        
        print(consoleGUI("separador","none","none"))
        key_code = int(input(consoleGUI("employee-insert-id","none","none")))
        

    return code, data 

def employeePosition():
    return

def employeeCompany():
    return

def employeeComission():
    return

#TIPO DE DATO NO EXISTENTE
def invalidParameter ():
  raise print(consoleGUI("error","No se encuentra el parametro solicitado","E-002"))
#FINALIZACIÓN DE LA ALERTA

def employeeSelectParameter (number):
    Parameter = {
        1: employeeName,
        2: employeeID,
        3: employeePosition,
        4: employeeCompany,
        5: employeeComission
    }
    selected = Parameter.get(number, invalidParameter)
    return selected()
