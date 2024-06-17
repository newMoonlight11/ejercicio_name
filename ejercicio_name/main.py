from clases import *
from gestorfile import *
info={}
users={}
isAddPerson=True
while isAddPerson:
    individuo=user()
    individuo.nombre=input("Ingrese el nombre: ")
    individuo.edad=int(input(f"Ingrese la edad de {individuo.nombre}: "))
    # isAddPhone=True
    # while isAddPhone:
    individuo.addPhone=int(input("Ingresa el número de teléfono: "))
        # isAddPhone=bool(input("Intro para salir, s para ingresar otro número..."))
        # users.update({len(users)+1:individuo})
    use={
            "nombre":individuo.nombre,
            "edad":individuo.edad,
            "telefono":individuo.addPhone
        }
    users.update({len(users)+1:use})
    isAddPerson=bool(input("Intro para salir, s para continuar..."))

info.update(users)
myFile=Archivos('midata.json',info)
myFile.Guardar(info)
print(myFile.Cargar())
