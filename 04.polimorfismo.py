class Restaurante:

    #constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, \nCategoría: {self.categoria}, Precio: {self.precio}")

        #GETTERS Y SETTERS (ASI SE MODIFICA LOS ATRIBUTOS ENCAPSULADOS)
        #Get = obtiene un valor
        #Set = Agrega un valor

    def get_precio(self):  #obtengo el valor private
        return self.__precio

    def set_precio(self, precio): #puedo a acceder al valor private y modificarlo a traves de un metodo
        self.__precio = precio

restaurante = Restaurante("Don Pepe", "Parrilla", 50)
#restaurante.__precio=80 #no se puede modificar, esta encapsulado
restaurante.mostrar_informacion()
restaurante.set_precio(80)
precio = restaurante.get_precio() #se guarda en una variable por el meétodo retorna un valor
print(precio)

restaurante2 = Restaurante("Il Gato", "Pastas", 20)
restaurante2.mostrar_informacion()
restaurante2.set_precio(60)
precio2 = restaurante2.get_precio()
print(precio2)
 
#Crear una clase hijo de Restaurante

class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, pileta):
        super().__init__(nombre, categoria, precio)
        self.pileta = pileta
    
    #Re-escribir un metodo debe llamarse igual
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, \nCategoría: {self.categoria}, Precio: {self.precio}, Pileta: {self.pileta}")
    
    
    #Agregar un metodo que solo exista en Hotel
    def get_pileta(self):
        return self.pileta

hotel = Hotel("Hotel POO", "5 Estrellas", 200, "Si")
hotel.mostrar_informacion()
pileta = hotel.get_pileta()
print(pileta)