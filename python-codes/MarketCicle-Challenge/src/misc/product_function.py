import time
from ..functions.gui import consoleGUI, clearGUI

def product(name, brand, color, size, price, iva, client, date,code):
    productObj = {
        "name": name,
        "brand": brand,
        "color": color,
        "size": size,
        "price": price,
        "iva": iva,
        "client": client,
        "date": date,
        "code": code
    }
    return productObj


def productName(productObj,client,date):
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


def productBrand(productObj,client,date):
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
                print(consoleGUI("product-insert-id-show",
                      "Marca de Bicicleta Specialized", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.brand = "Specialized"
                time.sleep(3)
            elif brand == 2:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Marca de Bicicleta Treck", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.brand = "Treck"
                time.sleep(3)
            elif brand == 3:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Marca de Bicicleta BMC", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.brand = "BMC"
                time.sleep(3)
    return productObj.brand, data, iterator


def productColor(productObj,client,date):
    iterator = productObj.iterator
    validation = False
    data = "color"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        color = int(input(consoleGUI("product-insert-color", "none", "none")))
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI("validation-data", "none", "none"))
        if key_validation.lower() == "si":
            print("Entrando")            
            if color == 1:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Color de Bicicleta Rojo", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.color = "Rojo"
                time.sleep(3)
            elif color == 2:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Color de Bicicleta Negro", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.color = "Negro"
                time.sleep(3)
            elif color == 3:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Color de Bicicleta Rojo-Negro", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.color = "Rojo-Negro"
                time.sleep(3)
    return productObj.color, data, iterator


def productSize(productObj,client,date):
    iterator = productObj.iterator
    validation = False
    data = "size"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        size = int(input(consoleGUI("product-insert-size", "none", "none")))
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI("validation-data", "none", "none"))
        if key_validation.lower() == "si":
            if size == 1:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Tamaño de Bicicleta S", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "S"
                time.sleep(3)
            elif size == 2:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Tamaño de Bicicleta M", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "M"
                time.sleep(3)
            elif size == 3:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Tamaño de Bicicleta L", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "L"
                time.sleep(3)
            elif size == 4:
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Tamaño de Bicicleta XL", "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.size = "XL"
                time.sleep(3)
    return productObj.size, data, iterator


def productPrice(productObj,client,date):    
    iterator = productObj.iterator
    validation = False
    data = "price"
    while validation == False:        
        clearGUI()
        print(consoleGUI("separador", "none", "none"))        
        price = input(consoleGUI("product-insert-price", "none", "none"))        
        if price.isnumeric():            
            disallowed_chars = "@+=&.,:;'"+'"'
            for character in disallowed_chars:
                price = price.replace(character, "")
            clearGUI()
            print(consoleGUI("separador", "none", "none"))
            key_validation = input(consoleGUI(
                "validation-data", "none", "none"))            
            if key_validation.lower() == "si":                
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "Precio de Bicicleta "+price, "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.price = price
                time.sleep(3)            
    return productObj.price, data, iterator


def productIva(productObj,client,date):
    iterator = productObj.iterator
    validation = False
    data = "iva"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        iva = input(consoleGUI("product-insert-iva", "none", "none"))
        if iva.isnumeric():
            disallowed_chars = "@+=&.,:;'"+'"'
            for character in disallowed_chars:
                iva = iva.replace(character, "")
            clearGUI()
            print(consoleGUI("separador", "none", "none"))
            key_validation = input(consoleGUI(
                "validation-data", "none", "none"))
            if key_validation.lower() == "si":
                clearGUI()
                print(consoleGUI("separador", "none", "none"))
                print(consoleGUI("product-insert-id-show",
                      "IVA de Bicicleta "+iva, "none"))
                print(consoleGUI("separador", "none", "none"))
                validation = True
                productObj.iva = iva
                time.sleep(3)
    return productObj.iva, data, iterator

def productClient(productObj,client,date):
    productObj.client = client
    return str(productObj.client)

def productDate(productObj,client,date):
    productObj.date = date
    return str(productObj.date)

# TIPO DE DATO NO EXISTENTE
def invalidParameter():
    raise print(consoleGUI(
        "error", "No se encuentra el parametro solicitado", "E-002"))
# FINALIZACIÓN DE LA ALERTA


def overWriteData(number, productObj):
    key_overwrite = "si"
    iterator = productObj.iterator    
    if number == 1 and productObj.name != "none":
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI(
            "overwrite-data", "\nProducto/Bicicleta "+productObj.name, "none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 2 and productObj.brand != "none":
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI(
            "overwrite-data", "\nProducto/Bicicleta "+productObj.name+" marca "+productObj.brand, "none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 3 and productObj.color != "none":
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI("overwrite-data", "\nProducto/Bicicleta " +
                              productObj.name+" marca "+productObj.brand+" color "+productObj.color, "none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 4 and productObj.size != "none":
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI("overwrite-data", "\nProducto/Bicicleta "+productObj.name+" marca " +
                              productObj.brand+" color "+productObj.color+" tamaño "+productObj.size, "none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 5 and productObj.price != 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI("overwrite-data", "\nProducto/Bicicleta "+productObj.name+" marca " +
                              productObj.brand+" color "+productObj.color+" tamaño "+productObj.size+" precio "+productObj.price, "none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    elif number == 6 and productObj.iva != 0:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI("overwrite-data", "\nProducto/Bicicleta "+productObj.name+" marca " +
                              productObj.brand+" color "+productObj.color+" tamaño "+productObj.size+" precio "+productObj.price+" con iva"+str(productObj.iva), "none"))
        iterator = productObj.iterator - 1
        productObj.iterator = iterator
    return key_overwrite, iterator


def exitFunction(productObj, client, date):
    iterator = 31
    return "none", "none", iterator


def productConfirmationData(productObj):
    clearGUI()
    iterator = productObj.iterator
    key_confirmation = input(consoleGUI(
        "confirmation-data", "Producto/Bicicleta", "none"))
    if key_confirmation == 1:
        iterator = iterator-1
    else:
        iterator = iterator+2
    return iterator, key_confirmation


def productSelectParameter(number, productObj, client, date):
    key_overwrite, productObj.iterator = overWriteData(number, productObj)
    if key_overwrite.lower() == "no":
        return "none", "none", productObj.iterator

    Parameter = {
        1: productName,
        2: productBrand,
        3: productColor,
        4: productSize,
        5: productPrice,
        6: productIva,
        7: exitFunction,
        8: productClient,
        9: productDate
    }

    selected = Parameter.get(number, invalidParameter)
    return selected(productObj, client , date)
