#Programa que agrera valores a un archivo vacio excel

import csv

#Lista de 3 numeros donde se agreran los valores
a=[[1,2,3]]

#Valores a agregar
["cafe","azucar","cremas"]
[12.50,18.01,16.54]

#Llamado del archivo
archivo= open("ejemplos2.cvs","w")

#Sentencia que escribe en el archivo
escribir= csv.writer(archivo)

#Ciclo que agrega en cada renglon los valores
for renglon in a:
    escribir.writerow(renglon)

#cierre de archivo
archivo.close()

