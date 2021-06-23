import json
import time
from tabulate import tabulate
import datetime
from ..functions.logic import generateProductCode
from ..functions.gui import consoleGUI, clearGUI
from ..misc.employee import Employee
from ..misc.product import Product
from ..misc.client import Client
from ..misc.employee_function import employee, employeeSelectParameter,employeeConfirmationData
from ..misc.client_function import client, clientSelectParameter,clientConfirmationData
from ..misc.product_function import product, productSelectParameter,productConfirmationData
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
        employeeObj.iterator = iterator
        if iterator == 31: break
        if employeeObj.name != "none" and employeeObj.code != "none" and employeeObj.position != "none" and employeeObj.company != None:
            iterator,key_confirmation = employeeConfirmationData(employeeObj)                        
            if int(key_confirmation) == 2:                
                break
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

    if iterator != 31:
        test = employeeObj.code
        employeeObj = employee(employeeObj.name, employeeObj.code,
                            employeeObj.position, employeeObj.company, str(employeeObj.comission))
        employeeDB["employee"].append(employeeObj)
        stateManagerWrite(json, employeeDB, 'database/Employee_db.json')

        employeePrint = -1
        for employ in employeeDB["employee"]:     
            employeePrint = employeePrint+1
            if employ["id"] == test:                  
                break 

        clearGUI()     
        print(consoleGUI("result-data-insert","VENDEDOR/EMPLEADO","none"))    
        return input(tabulate([employeeDB["employee"][employeePrint]],headers='keys',tablefmt="psql")+"\n\nContinuar? -> ")
    return
    


def insertProduct(name,brand,color,size,price,iva,client,date,code):
    productObj = Product(name,brand,color,size,price,iva,client,date,code)   
    clearGUI()
    print(consoleGUI("separador", "none", "none"))
    print(consoleGUI("product-insert-select", "none", "none"))
    productDB = stateManagerRead(json, 'database/Product_db.json')
    key_update = int(
        input(consoleGUI("product-insert-options", "none", "none")))

    while key_update > 7 or key_update < 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        print(consoleGUI("error", "Ha ocurrido un error en la selección," +
                         " porfavor dígite alguna de las opciones que se encuentran en pantalla", "001"))
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI(
            "product-insert-options", "none", "none")))
    
    iterator = 0     
    while productObj.iterator <= 6:
        productObj.iterator = iterator + 1                        
        data, dataType, iterator = productSelectParameter(key_update, productObj,productObj.client,productObj.date)                           
        productObj.iterator = iterator        
        if iterator == 31: break
        if productObj.name != "none" and productObj.brand != "none" and productObj.color != "none" and productObj.size != "none" and productObj.price != 0 and productObj.iva != 0:
            iterator, key_confirmation = productConfirmationData(productObj)
            if int(key_confirmation) == 2: 
                productObj.code = generateProductCode()
                productObj.date = str(datetime.datetime.now())
                break
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(
            input(consoleGUI("product-insert-options", "none", "none")))
        if dataType == "name":            
            productObj.name = data
        elif dataType == "brand":            
            productObj.brand = data
        elif dataType == "color":            
            productObj.color = data
        elif dataType == "size":            
            productObj.size = data
        elif dataType == "price":            
            productObj.price = data
        elif dataType == "iva":            
            productObj.iva = data       

    if iterator != 31:
        productCode = productObj.code
        productObj = product(productObj.name, productObj.brand,productObj.color,productObj.size,productObj.price,productObj.iva,productObj.client,productObj.date,productObj.code)
        productDB["product"].append(productObj)
        stateManagerWrite(json, productDB, 'database/Product_db.json')

        productPrint = -1
        for prod in productDB["product"]:     
            productPrint = productPrint+1
            print(prod)
            if prod["code"] == productCode:                  
                break 

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
            
        print(consoleGUI("result-data-insert","PRODUCTO/BICICLETA","none"))    
        return input(tabulate([productDB["product"][productPrint]],headers='keys',tablefmt="psql")+"\n\nContinuar? -> ")
    return

def insertClient(name,code,product,total_price,amount_products):
    clientObj = Client(name, code, product, total_price, amount_products)   
    clearGUI()
    print(consoleGUI("separador", "none", "none"))
    print(consoleGUI("client-insert-select", "none", "none"))
    productDB = stateManagerRead(json, 'database/Product_db.json')
    clientDB = stateManagerRead(json, 'database/Client_db.json')
    key_update = int(
        input(consoleGUI("client-insert-options", "none", "none")))

    while key_update > 3 or key_update < 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        print(consoleGUI("error", "Ha ocurrido un error en la selección," +
                         " porfavor dígite alguna de las opciones que se encuentran en pantalla", "001"))
        print(consoleGUI("separador", "none", "none"))
        key_update = int(input(consoleGUI(
            "client-insert-options", "none", "none")))
    
    iterator = 0     
    while clientObj.iterator <= 2:
        clientObj.iterator = iterator + 1                        
        data, dataType, iterator = clientSelectParameter(key_update, clientObj)                           
        clientObj.iterator = iterator        
        if iterator == 31: break
        if clientObj.name != "none" and clientObj.product != []:
            iterator, key_confirmation = clientConfirmationData(clientObj)
            if int(key_confirmation) == 2:                 
                clientObj.code = generateProductCode()                
                clientObj.amount_products = len(productDB["product"])                
                break
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_update = int(
            input(consoleGUI("client-insert-options", "none", "none")))
        if dataType == "name":            
            clientObj.name = data            
        elif dataType == "product":            
            clientObj.product = data   

    codeProductObj = "none"  
    
    if iterator != 31:        
        iteratorProduct = 0
        for productObj in productDB["product"]:                 
            for productsObj in clientObj.product:                
                if productObj["code"] == productsObj["code"]: 
                    codeProductObj = productObj["code"] 
                    clientCode = clientObj.code
                    clientObj = client(clientObj.name, clientObj.code,clientObj.product,clientObj.total_price,clientObj.amount_products)
                    productDB["product"][iteratorProduct]["client"].append(clientObj)
                    clientObj = Client(clientObj["name"], clientObj["code"], clientObj["product"], clientObj["total_price"],clientObj["amount_products"])        
                    stateManagerWrite(json,productDB,'database/Product_db.json')                
                    time.sleep(1)
            iteratorProduct = iteratorProduct+1        

        for productData in productDB["product"]:  
            if productData["client"] != None:                
                for itemSum in productData["client"]:                                        
                    if str(itemSum["code"]) == str(clientObj.code):
                        clientObj.total_price = int(clientObj.total_price)                                               
                        clientObj.total_price = clientObj.total_price+(int(productData["price"])+((int(productData["iva"])*100)/int(productData["price"])))

        clientObj = client(clientObj.name, clientObj.code,clientObj.product,clientObj.total_price,clientObj.amount_products)
        clientDB["client"].append(clientObj)        
        stateManagerWrite(json, clientDB, 'database/Client_db.json')

        clientPrint = -1
        for cli in clientDB["client"]:     
            clientPrint = clientPrint+1
            print(cli)
            if cli["code"] == clientCode:                  
                break 

        clearGUI()     
        print(consoleGUI("result-data-insert","CLIENTE","none"))    
        clientNameProduct = []
        iteratorExport = 0
        for clientData in clientDB["client"]:  
            for products in clientData["product"]:
                if clientData["code"] == clientObj["code"]:
                    clientNameProduct.append("Producto: "+str(products["name"])+" - ID: "+str(products["code"]))
                    clientData["product"] = clientNameProduct
            iteratorExport = iteratorExport +1
            input(tabulate([clientDB["client"][clientPrint]],headers='keys',tablefmt="psql")+"\n\nContinuar? -> ")
        return codeProductObj
    return    
