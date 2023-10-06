import os
import shutil

#os.mkdir("Documentos_Archivos")

from_dir='/Users/migue/Desktop/Python/New folder/'
to_dir='/Users/migue/Desktop/Python/New folder/Documentos_Archivos/'

list_of_files= os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    root,extencion= os.path.splitext(i)
    print(f"Nombre: {root}, Extensión: {extencion}")
  


