# Escritura en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:
    file.write("Primera nota personal: Aprendiendo archivos Python.\n")
    file.write("Segunda nota personal: Realizare el archivo de texto.\n")
    file.write("Tercera nota personal: Subiré este código para mi tarea.\n")
    # Puedes agregar más notas si lo deseas

# Lectura del archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    line = file.readline()  # Lee la primera línea
    while line:  # Mientras haya líneas para leer
        print(line.strip())  # Muestra la línea eliminando el salto de línea adicional
        line = file.readline()  # Lee la siguiente línea

