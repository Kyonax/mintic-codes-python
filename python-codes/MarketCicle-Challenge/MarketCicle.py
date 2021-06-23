from src.modules.insert import insertEmployee, insertProduct, insertClient
from src.modules.remove import removeEmployee, removeProduct, removeClient
from src.modules.toList import toListEmployees, toListProducts


key_option = int(input("OPCIONES\n[1] Employee Insert\n[2] Product Insert\n[3] Client Insert\n[4] Eliminar Cliente\n\n-> "))

if key_option == 1:
    insertEmployee("none","none","none",None,0)    
elif key_option == 2:
    insertProduct("none","none","none","none",0,0,[],"none","none")
elif key_option == 3:
    insertClient("none","none",[],0,0)
elif key_option == 4:
    removeClient("M2*0002M")
elif key_option == 5:
    toListProducts()
else:
    print("no entra")