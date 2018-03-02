from VALID import ns, OKI
import pickle
import subprocess

def opcion():
    while True:
        op=input("Escriba opción: ")
        if op==("A") or op==("B") or op==("C"):
            break
    return op

while True:
    print("A)VER CAMPOS ACTUALES")
    print("B)AÑADIR CAMPOS")
    print("C)ELIMINAR CAMPOS")
    elec=opcion()
    campos=pickle.load(open("marcador.mio","rb"))
    if elec==("A"):
        print("")
        print("ESTADO ACTUAL: ",campos)
        print("")

    elif elec==("B"):
        numero_campos=OKI(input("Escriba el número de campos que desea añadir al marcador: "))
        numcam=(len(campos))-1
        cam_nuevos=[]
        n=0
        while n<numero_campos:
            campos.append(0)
            numcam+=1
            cam_nuevos.append(numcam)
            n+=1
        print("")
        print("NUEVO ESTADO: ",campos)
        print("POSICIONES AÑADIDAS: ",cam_nuevos)
        print("")
    elif elec==("C"):
        numero_campos=OKI(input("Escriba el número de campos que desea eliminar del marcador: "))
        while numero_campos>len(campos):
            numero_campos=OKI(input("El número de campos especificado es superior al número de campos actual: "))
        numcam=(len(campos))-1
        cam_eliminad=[]
        n=0
        while n<numero_campos:
            #el=campos.pop()
            cam_eliminad.append(numcam)
            numcam-=1
            del campos[-1]
            n+=1
        cam_eliminad.sort()
        print("")
        print("NUEVO ESTADO: ",campos)
        print("POSICIONES ELIMINADAS: ",cam_eliminad)
        print("")
    pickle.dump(campos,open("marcador.mio","wb"))
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
