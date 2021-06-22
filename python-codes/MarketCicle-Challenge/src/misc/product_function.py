import time
import json
from ..functions.gui import consoleGUI, clearGUI
from ..functions.logic import generateCode, createCode
from .product import Product
from ..functions.stateManager import stateManagerRead


def product(name, brand,color,size,price,iva,client,date):
    productObj = {
        "name": name,
        "brand": brand,
        "color": color,
        "size": size,
        "price": price,
        "iva": iva,
        "client": client,
        "date": date
    }
    return productObj


def productName(productObj):    
    iterator = productObj.iterator
    validation = False
    data = "name"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))        
        name = input(consoleGUI("product-insert-name", "none", "none"))        
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI("validation-data", "none", "none"))
        if key_validation.lower() == "si":
            validation = True            
            productObj.name = name                    
    return name, data, iterator


def productBrand(productObj):    
    iterator = productObj.iterator
    validation = False
    data = "brand"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        brand = int(input(consoleGUI("product-insert-id", "none", "none")))
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI(
            "validation-selection", "none", "none"))
        if key_validation.lower() == "si":
            if brand == 1:                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Marca de Bicicleta Specialized", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.brand = "Specialized"
                time.sleep(3)
            elif brand == 2:                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Marca de Bicicleta Treck", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.brand = "Treck"
                time.sleep(3)        
            elif brand == 3:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Marca de Bicicleta BMC", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.brand = "BMC"
                time.sleep(3)        
    return productObj.brand, data, iterator


def productColor(productObj):
    iterator = productObj.iterator
    validation = False
    data = "color"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        color = input(consoleGUI("product-insert-color","none","none"))
        clearGUI()
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))
        if key_validation.lower() == "si":
            if color == 1:                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Color de Bicicleta Rojo", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.color = "Rojo"
                time.sleep(3)
            elif color == 2:                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Color de Bicicleta Negro", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.color = "Negro"
                time.sleep(3)        
            elif color == 3:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Color de Bicicleta Rojo-Negro", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.color = "Rojo-Negro"
                time.sleep(3)            
    return productObj.color, data, iterator


def productSize(productObj):
    iterator = productObj.iterator
    validation = False
    data = "size"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        size = input(consoleGUI("product-insert-size","none","none"))
        clearGUI()
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))
        if key_validation.lower() == "si":
            if size == 1:                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Tamaño de Bicicleta S", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "S"
                time.sleep(3)
            elif size == 2:                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Tamaño de Bicicleta M", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "M"
                time.sleep(3)        
            elif size == 3:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Tamaño de Bicicleta L", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "L"
                time.sleep(3)  
            elif size == 4:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show", "Tamaño de Bicicleta XL", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "XL"
                time.sleep(3) 
    return productObj.size, data, iterator



def productPrice(productObj):
    iterator = productObj.iterator
    validation = False
    data = "price"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        price = input(consoleGUI("product-insert-price","none","none"))
        disallowed_chars = "@+=&.,:;'"+'"'
        for character in disallowed_chars:
	        price = price.replace(character, "")
        clearGUI()
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))
        if key_validation.lower() == "si":
            clearGUI()
            print(consoleGUI("separador", "none", "none"))
            print(consoleGUI("product-insert-id-show", "Precio de Bicicleta "+price, "none"))
            print(consoleGUI("separador", "none", "none"))
            validation = True
            productObj.price = price
            time.sleep(3) 
    return productObj.price, data, iterator

def productIva(productObj):
    iterator = productObj.iterator
    validation = False
    data = "iva"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        iva = input(consoleGUI("product-insert-iva","none","none"))
        disallowed_chars = "@+=&.,:;'"+'"'
        for character in disallowed_chars:
	        iva = iva.replace(character, "")
        clearGUI()
        print(consoleGUI("separador","none","none"))
        key_validation = input(consoleGUI("validation-data","none","none"))
        if key_validation.lower() == "si":
            clearGUI()
            print(consoleGUI("separador", "none", "none"))
            print(consoleGUI("product-insert-id-show", "IVA de Bicicleta "+iva, "none"))
            print(consoleGUI("separador", "none", "none"))
            validation = True
            productObj.iva = iva
            time.sleep(3) 
    return productObj.iva, data, iterator

# TIPO DE DATO NO EXISTENTE


def invalidParameter():
    raise print(consoleGUI(
        "error", "No se encuentra el parametro solicitado", "E-002"))
# FINALIZACIÓN DE LA ALERTA


def overWriteData(number,productObj):                 
    key_overwrite = "si"
    iterator = productObj.iterator    
    if number == 1 and productObj.name != "none":
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+productObj.name,"none"))        
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 2 and productObj.code !=  "none":
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+productObj.name+" código "+productObj.code,"none"))        
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 3 and productObj.position != "none":
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+productObj.name+" código "+productObj.code+" Cargo "+productObj.position,"none"))        
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 4 and productObj.company != None:
        clearGUI()        
        print(consoleGUI("separador","none","none"))        
        key_overwrite = input(consoleGUI("overwrite-data","\nVendedor/Empleado "+productObj.name+" código "+productObj.code+" Cargo "+productObj.position+" de la Compañia "+productObj.company,"none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator    
    return key_overwrite,iterator   
    
def exitFunction(productObj,comission):
    iterator = productObj.iterator + 7
    return "none", "none", iterator

def productConfirmationData (productObj):
    clearGUI()
    iterator = productObj.iterator
    key_confirmation = input(consoleGUI("confirmation-data","Vendedor/Empleado","none"))
    if key_confirmation == 1:        
        iterator = iterator-1        
    else:
        iterator = iterator+2
    return iterator


def productSelectParameter(number,productObj,comission):  
    key_overwrite, productObj.iterator = overWriteData(number,productObj)                                 
    if key_overwrite.lower() == "no":
        return "none","none",productObj.iterator

    Parameter = {
        1: productName,
        2: productID,
        3: productPosition,
        4: productCompany,
        5: exitFunction,
        6: productComission
    }      
     
    selected = Parameter.get(number, invalidParameter)    
    return selected(productObj,comission)

    
