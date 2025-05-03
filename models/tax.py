class Tax:
    def __init__(self, name: str, rate: float):
        self.__name = name        
        self.__rate = rate 

    @property
    def name(self):
        return self.__name
    
    @property
    def rate(self):
        return self.__rate

    @name.setter
    def name(self, name):
        self.__name = name

    @rate.setter
    def type(self, rate):
        self.__rate = rate
