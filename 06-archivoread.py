def app():
    with open("udemy.txt", "r") as f:
        for contenido in f:
            print(contenido.rstrip()) #rstrip(remove strip) elimina los saltos de linea

app()