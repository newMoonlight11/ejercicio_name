import json
class Archivos:
    def __init__(self,archivo:str,info:dict):
        self.__archivo=archivo
        self.__infodata=info

    def Guardar(self,info:dict):
        with open('data/'+self.__archivo, "w") as write_file:
            json.dump(self.__infodata, write_file,indent = 4)
            write_file.close()
    def Cargar(self):
        with open('data/'+self.__archivo, "r") as read_file:
            info = json.load(read_file)
        return info
    def Borrar(self,info:dict,llave:str):
        with open('data/'+self.__archivo, "r") as read_file:
            self.__infodata = json.load(read_file)
        info.pop(llave)
        self.Guardar(info)