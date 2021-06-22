class Employee(object):
    def __init__(self,name,code,position,company,comission):
        self._iterator = 0        
        self._name = name
        self._code = code
        self._position = position
        self._company = company
        self._comission = comission

    @property
    def iterator(self):
        return self._iterator

    @iterator.setter
    def iterator(self,x):
        self._iterator = x
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,x):
        self._name = x
    
    @property
    def code(self):
        return self._code 
    
    @code.setter
    def code(self,x):
        self._code = x
    
    @property    
    def position(self):
        return self._position
    
    @position.setter
    def position(self,x):
        self._position = x
    
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self,x):
        self._company= x
    
    @property
    def comission(self):
        return self._comission

    @comission.setter
    def comission(self,x):
        self._comission = x

