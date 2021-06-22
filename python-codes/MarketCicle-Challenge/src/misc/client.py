class Client(object):
    def __init__(self,name,code,product,price,amount):
        self._iterator = 0        
        self._name = name
        self._code = code
        self._product = product
        self._price = price
        self._amount = amount

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
    def product(self):
        return self._product
    
    @product.setter
    def product(self,x):
        self._product = x
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,x):
        self._price= x
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self,x):
        self._amount = x
