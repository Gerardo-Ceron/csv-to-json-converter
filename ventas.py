import csv
import json

# Datos de ejemplo (simulando un archivoCSV)

datos_csv = """Producto,Cantidad
Laptop,800
Mouse,25
Teclado,45
Monitor,150
Cable HDMI,15"""

#Guardamos el ejemplo en un archivo local
with open("ventas.csv", "w", newline="") as f:
    f.write(datos_csv)

# SCRIPT DE AUTOMATIZACIÓN
lista_ventas = []

with open("ventas.csv", "r") as archivo_csv:
    reader = csv.DictReader(archivo_csv)
    for row in reader:
        lista_ventas.append(row)

# Guardar los datos en un archivo JSON
with open("ventas.json", "w") as archivo_json:
    json.dump(lista_ventas, archivo_json, indent=4)
    print("Datos exportados a ventas.json con éxito.")