playlist = {} #diccionario vacio
playlist["canciones"] = [] #Lista Vacia

#Funcion Principal
def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input("¿Cómo deseas nombrar la Playlist?: \r\n")
        if nombre_playlist:
            playlist["nombre"] = nombre_playlist
            #ya tenemos un nombre de playlist, desactivamos el True
            agregar_playlist = False
            
            #mandamos a llamar a la funcion de agregar canciones
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True
    while agregar_cancion:
        nombre_cancion = input("¿Agrega el Título de la canción?: \r\n")
        if nombre_cancion:
            playlist["canciones"].append(nombre_cancion)
            #ya tenemos un nombre de playlist, desactivamos el True
            rta = input("Desea agregar otra canción? si/no: \r\n")
            if rta == "no":
                agregar_cancion = False
                mostrar_resumen()            

def mostrar_resumen():
    nombre_playlist = playlist["nombre"]
    print(f"Playlist: \n{nombre_playlist}\r\n")
    print(f"Canciones\r\n")
    for cancion in playlist["canciones"]:
        print(cancion)
    
app()
