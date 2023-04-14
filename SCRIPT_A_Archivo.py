import os,json

ruta_archivo_actual = os.path.abspath(__file__)
directorio_PATH= os.path.dirname(ruta_archivo_actual)

try:
    linea=int(input("\n Numero De Linea : "))
except:
    exit()

with open('linesprog.json') as f:
    json_data = f.read()
data_dict = json.loads(json_data)

Archivo ="" ; minimo  =0 ; maximo = 1 

for archivo in data_dict:
    data_archivo=data_dict[archivo]
    min_a=data_archivo["min"]
    max_a=data_archivo["max"]

    if min_a<linea and linea<=max_a:
        Archivo=archivo
        minimo=min_a
        maximo=max_a

if Archivo != "":
    directorio_codigo=os.path.join(directorio_PATH,"codigo")
    directorio_archivo=os.path.join(directorio_codigo,Archivo)
    linea_para_vim="vim +"+str(linea-minimo)+" "+str(directorio_archivo)+""
    os.system(linea_para_vim)

