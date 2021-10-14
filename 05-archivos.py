with open("udemy.txt", "w") as f: # w es escritura y si no existe lo crea   
    #generar nros en archivos
    for i in range(0, 20):
        f.write("Esta es la linea " + str(i) + "\r\n")
        