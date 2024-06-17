class user():
    def __init__(self):
        self.__nombre=''
        self.__edad=0
        self.__telefono={}

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, new_value):
            self.__nombre = new_value

        @nombre.deleter
        def nombre(self):
            del self.__nombre
        
        @property
        def edad(self):
            return self.__edad

        @edad.setter
        def edad(self, new_value):
            self.edad=new_value

        @edad.deleter
        def edad(self):
            del self.__edad
        @property
        def telefono(self):
            return self.__telefono
        
        @telefono.deleter
        def telefono(self):
            del self.__telefono

        def addPhone(self,idioma):
            self.__telefono.update({len(self.__telefono)+1:telefono})