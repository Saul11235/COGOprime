#puts program codeon the OS clipboard
import pyperclip,os

ruta_archivo_actual = os.path.abspath(__file__)
directorio_PATH= os.path.dirname(ruta_archivo_actual)

f=open("program.hpprog","r")
pyperclip.copy(f.read())
f.close()

print(directorio_PATH)
print("programa en memoria :) ")
if __name__=="__main__":
    input("ok")
