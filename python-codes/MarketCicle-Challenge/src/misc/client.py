class Client(object):
    def __init__(self,name,code,product,total_price,amount_products):
        self._iterator = 0        
        self._name = name
        self._code = code
        self._product = product
        self._total_price = total_price
        self._amount_products = amount_products

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
    def total_price(self):
        return self._total_price
    
    @total_price.setter
    def total_price(self,x):
        self._total_price= x
    
    @property
    def amount_products(self):
        return self._amount_products

    @amount_products.setter
    def amount_products(self,x):
        self._amount_products = x
