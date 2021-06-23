import time
import json
from ..functions.gui import consoleGUI, clearGUI
from ..functions.logic import generateCode
from ..functions.stateManager import stateManagerRead


def client(name, code, product, total_price, amount_products):
    clientObj = {
        "name": name,
        "code": code,
        "product": product,
        "total_price": total_price,
        "amount_products": amount_products
    }
    return clientObj


def clientName(clientObj):
    iterator = clientObj.iterator
    validation = False
    data = "name"
    while validation == False:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        name = input(consoleGUI("client-insert-name", "none", "none"))
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI("validation-data", "none", "none"))
        if key_validation.lower() == "si":
            validation = True
            clientObj.name = name
    return name, data, iterator


def clientProduct(clientObj):
    iterator = clientObj.iterator
    validation = False
    data = "product"
    while validation == False:
        clearGUI()
        productDB = stateManagerRead(json, 'database/Product_db.json')
        amountProductsDB = []
        for data in productDB["product"]:
            amountProductsDB.append(data["name"]+" - Marca: "+data["brand"]+" - Color: "+data["color"]+" - Tamaño: " +
                                    data["size"]+" - ID: "+data["code"]+" | Valor COP: $"+str(data["price"])+" + IVA del "+str(data["iva"])+"%"+" | Total: $"+str(int(data["price"])+((int(data["iva"])*100)/int(data["price"]))))

        optionData = ""
        iteratorData = 0
        for dataStr in amountProductsDB:            
            optionData = optionData+"["+str(iteratorData)+"] "+dataStr+"\n"
            iteratorData = iteratorData + 1

        print(consoleGUI("separador", "none", "none"))
        product = input(consoleGUI("client-insert-product",
                        optionData, "none"))
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_validation = input(consoleGUI("validation-data", "none", "none"))
        if key_validation.lower() == "si":
            clearGUI()
            print(consoleGUI("separador", "none", "none"))
            print(consoleGUI("product-insert-id-show","Producto "+amountProductsDB[int(product)], "none"))
            print(consoleGUI("separador", "none", "none"))
            validation = True
            clientObj.product = productDB["product"][int(product)]
            time.sleep(3)
    return clientObj.product, data, iterator

# TIPO DE DATO NO EXISTENTE
def invalidParameter():
    raise print(consoleGUI(
        "error", "No se encuentra el parametro solicitado", "E-002"))
# FINALIZACIÓN DE LA ALERTA


def overWriteData(number, clientObj):
    key_overwrite = "si"
    iterator = clientObj.iterator
    if number == 1 and clientObj.name != "none":
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI(
            "overwrite-data", "\nCliente "+clientObj.name, "none"))
        iterator = clientObj.iterator - 1
        clientObj.iterator = iterator
    elif number == 2 and clientObj.product != None:
        clearGUI()
        print(consoleGUI("separador", "none", "none"))
        key_overwrite = input(consoleGUI(
            "overwrite-data", "\nProducto "+clientObj.name+" producto "+clientObj.product["Name"]+" de Código "+clientObj.product["code"], "none"))
        iterator = clientObj.iterator - 1
        clientObj.iterator = iterator    
    return key_overwrite, iterator


def exitFunction():
    iterator = 31
    return "none", "none", iterator


def clientConfirmationData(clientObj):
    clearGUI()
    iterator = clientObj.iterator
    key_confirmation = input(consoleGUI(
        "confirmation-data", "Cliente y la nueva Venta.", "none"))
    if key_confirmation == 1:
        iterator = iterator-1
    else:
        iterator = iterator+2
    return iterator


def clientSelectParameter(number, clientObj):
    key_overwrite, clientObj.iterator = overWriteData(number, clientObj)
    if key_overwrite.lower() == "no":
        return "none", "none", clientObj.iterator

    Parameter = {
        1: clientName,
        2: clientProduct,        
        3: exitFunction
    }

    selected = Parameter.get(number, invalidParameter)
    return selected(clientObj)
