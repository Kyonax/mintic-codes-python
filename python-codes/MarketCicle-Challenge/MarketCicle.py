from src.modules.insert import insertEmployee, insertProduct

key_option = int(input("OPCIONES\n[1] Employee Insert\n[2] Product Insert\n\n-> "))

if key_option == 1:
    insertEmployee("none","none","none",None,0)    
elif key_option == 2:
    insertProduct("none","none","none","none",0,0,None,"none","none")
else:
    print("no entra")