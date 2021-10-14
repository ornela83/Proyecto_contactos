nota = 0
respuesta_1 = input("La Tierra esta mas cerca del sol que Marte. SI/NO: ")
respuesta_2 = input("Marte tiene dos lunas?. SI/NO: ")
respuesta_3 = input("Venus es el planeta mas cercano al sol?. SI/NO: ")

if respuesta_1.lower() == "si":
    nota += 1
if respuesta_2.lower() == "si":
    nota += 1
if respuesta_3.lower() == "no":
    nota += 1

print(f"Tenes {nota} respuestas correctas")

        

