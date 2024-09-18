
print(" \n Programacion POO")
# Definicion de clases 
class perrito:
    # Funciones  dentro de la clase 
    nombre="Boby"
    edad=4
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self, nombre,edad):
        print(f"  Nombre: {nombre} Edad : {edad}")

#Zona de creacion de objetos
pitbull=perrito()

#Zona de uso de objetos
pitbull.Datos_perro(" Boby ", 4)
pitbull.morder( )
