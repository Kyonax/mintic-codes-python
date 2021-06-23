class Product(object):
    def __init__(self,name,brand,color,size,price,iva,client,date,code):
        self._iterator = 0        
        self._name = name
        self._brand = brand
        self._color = color
        self._size = size
        self._price = price
        self._iva = iva
        self._client = client
        self._date = date
        self._code = code

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
    def brand(self):
        return self._brand 
    
    @brand.setter
    def brand(self,x):
        self._brand = x
    
    @property    
    def color(self):
        return self._color
    
    @color.setter
    def color(self,x):
        self._color = x
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,x):
        self._size= x
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,x):
        self._price = x

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self,x):
        self._client = x

    @property
    def iva(self):
        return self._iva

    @iva.setter
    def iva(self,x):
        self._iva = x

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self,x):
        self._date = x

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self,x):
        self._code = x