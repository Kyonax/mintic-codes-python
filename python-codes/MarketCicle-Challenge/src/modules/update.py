import json
import time
from tabulate import tabulate
from ..functions.gui import consoleGUI, clearGUI
from .insert import insertEmployee, insertProduct, insertClient
from ..functions.stateManager import stateManagerRead, stateManagerWrite, stateManagerConsole

def updateEmployee():
    clearGUI()
    print(consoleGUI("update-data","Empleados","none"))    
    return

def updateProduct():
    return

def updateClient():
    return
