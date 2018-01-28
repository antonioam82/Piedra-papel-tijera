from VALID import ns, OKI
import pickle
import subprocess

def opcion():
    while True:
        op=input("Escriba opción: ")
        if op==("A") or op==("B"):
            break
    return op

while True:
    print("A)VER CAMPOS ACTUALES")
    print("B)AÑADIR CAMPOS")
    elec=opcion()
    campos=pickle.load(open("marcador.mio","rb"))
    if elec==("A"):
        print("")
        print("ESTADO ACTUAL: ",campos)
        print("")

    else:
        numero_campos=OKI(input("Escriba el número de campos que desea añadir al marcador: "))
        n=0
        while n<numero_campos:
            campos.append(0)
            n+=1
        print("")
        print("NUEVO ESTADO: ",campos)
        print("")
    pickle.dump(campos,open("marcador.mio","wb"))
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
