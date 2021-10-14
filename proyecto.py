import os

CARPETA = "contactos/" #Esta en mayuscula para expresar que es una constante y no se debe modificar el valor  
EXTENSION = ".txt"  #estensión de archivos

#Crear una clase de Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    #Muestra el menú de opciones
    mostrar_resumen()

    #Preguntar al Usuario la accion a realizar

    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opción: \n")
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print("Opcion no válida, intente de nuevo")

def eliminar_contacto():
    nombre = input("Seleccione un Contacto que desea eliminar: \n")

    try: 
        os.remove(CARPETA + nombre + EXTENSION)
        print("\n Eliminado Correctamente")

    except:
        print("Ese contacto no existe")

    #Re iniciar la app()
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA) #crea una lista de los archivos que estan en la carpeta 

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] #recorre el iterador buscando los archivos terminados en .txt

    for archivo in archivos_txt:
        with open(CARPETA + archivo, encoding='utf8') as contacto:
            for linea in contacto:
                print(linea.rstrip()) #.rstrip elimina los saltos de linea
            print("\n") #imprime  separador

def buscar_contacto():
    nombre = input("Seleccione un Contacto que desea buscar: \n")

    try: 
        with open(CARPETA + nombre + EXTENSION, encoding="utf8") as contacto:
            print("\n Informacion del Contacto\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\n")
    except IOError:
        print("El archivo no existe")
        print(IOError)

    #Re iniciar la app()
    app()

def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior = input("Nombre del contacto que desea editar: \n")

    #Revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        print("Puedes editar")
        with open(CARPETA + nombre_anterior + EXTENSION, "w", encoding="utf8") as archivo:

            nombre_contacto = input("Agregar el nuevo nombre: \n")
            telefono_contacto = input("Agrega el nuevo Teléfono: \n")
            categoria_contacto = input("Agregar la nueva Categoría: \n")

            #Instanciar el objeto editado
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            #Escribir en el Archivo
            archivo.write("Nombre: " + contacto.nombre + "\n")
            archivo.write("Teléfono: " + contacto.telefono + "\n")
            archivo.write("Categoría: " + contacto.categoria + "\n")

            #Renombrar el Archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        print("\n Contacto editado correctamente \n")
    else:
        print("Ese contacto no existe")
    
    #Reiniciar la app()
    app()

def agregar_contacto():
    print("Escribe los datos para agregar el nuevo Contacto")
    nombre_contacto = input("Nombre del Contacto: \n")

    #Revisar si el nombre ya existe
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, "w", encoding="utf8") as archivo: #carpeta/ornela.txt

            #resto de los campos
            telefono_contacto = input("Agrega el Teléfono: \n")
            categoria_contacto = input("Categoría Contacto: \n")

            #Instaciar la clase(creamos el objeto)
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el Archivo
            archivo.write("Nombre: " + contacto.nombre + "\n")
            archivo.write("Teléfono: " + contacto.telefono + "\n")
            archivo.write("Categoría: " + contacto.categoria + "\n")

            #Mostrar mensaje de éxito
            print("\n Contacto creado correctamente \n")
    else:
        print("Ese contacto ya existe")

    #Reiniciar App
    app()

def mostrar_resumen():
    print("Seleccione del Menú lo que desee hacer: ")
    print("1) Agrega nuevo Contacto: ")
    print("2) Editar Contacto: ")
    print("3) Ver Contactos: ")
    print("4) Buscar Contacto: ")
    print("5) Eliminar Contacto: ")

def crear_directorio():
    if not os.path.exists(CARPETA): #si esta carpeta no existe, entonces la crea:
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    #Revisar si el nombre ya existe
    return os.path.isfile(CARPETA + nombre + EXTENSION)   

app()