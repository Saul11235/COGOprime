import os, re, json
from os import system, remove

ruta_archivo_actual = os.path.abspath(__file__)
directorio_PATH= os.path.dirname(ruta_archivo_actual)

# PARTE 1 creando codigo programas hp prime 

ruta_codigo = os.path.join(directorio_PATH, 'codigo')
nombres_archivos = os.listdir(ruta_codigo)
patron_tex = re.compile(r'.*\.hpprog$')
nombres_archivos= [archivo for archivo in nombres_archivos if patron_tex.match(archivo)]
nombres_archivos= sorted(nombres_archivos)

# PARTE 2 juntando archivo programas hp prime 

cod_prog="" 
contadorLineas=0
datos_lineas={}
# lista anidada [ [nombre_Archivo LineaInicio LineaFinal ]]
#                respecto a codigo programa_apilado
for archivo in nombres_archivos:
    primero=contadorLineas
    ruta_archivo=os.path.join(ruta_codigo,archivo)
    f=open(ruta_archivo,"r")
    for line in f.readlines():
        cod_prog+=line
        contadorLineas+=1
    f.close()
    datos={
            "min":primero,
            "max":contadorLineas
            }
    datos_lineas[archivo]=datos

# PARTE 4 escribiendo archivos 
f=open("program.hpprog","w")
f.write(cod_prog)
f.close()

with open("linesprog.json", "w") as f:
    json.dump(datos_lineas, f)

# PARTE 5 mensaje 
print(directorio_PATH)    

import SCRIPT_copiar_a_portapapeles

if __name__=="__main__":
    input("ok")
