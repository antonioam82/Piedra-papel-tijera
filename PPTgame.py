#PARA LA EJECUCIÓN DEL PROGRAMA SE NECESITAN LOS ARCHIVOS "VALID.py" y "marcador.mio.py" PRESENTES EN EL REPOSITORIO.
from VALID import ns
import random
import pickle
import subprocess

while True:
    print("JUGANDO A PIEDRA, PAPEL O TIJERA")
    Comp=random.choice(["piedra","papel","tijera"])
    Tu=input("Piedra, Papel o Tijera: ")
    Tu=Tu.lower()
    while Tu!=("piedra") and Tu!=("papel") and Tu!=("tijera"):
        Tu=input("Escribe solo \'piedra\',\'papel\' o \'tijera\'según su opción: ")
        Tu=Tu.lower()
    print("Tu:",Tu.upper())
    print("Ordenador:",Comp.upper())
    
    puntos=pickle.load(open("marcador.mio","rb"))
    if Tu!=Comp:   
        if Tu==("papel") and Comp==("tijera"):
            print("PERDISTE: Las tijeras cortan el papel")
            puntos[0]=puntos[0]+1;puntos[2]=puntos[2]+1
        if Tu==("papel") and Comp==("piedra"):
            print("GANASTE: El papel envuelve la piedra")
            puntos[0]=puntos[0]+1;puntos[1]=puntos[1]+1
        if Tu==("piedra") and Comp==("papel"):
            print("PERDISTE: El papel envuelve la piedra")
            puntos[0]=puntos[0]+1;puntos[2]=puntos[2]+1
        if Tu==("piedra") and Comp==("tijera"):
            print("GANASTE: La piedra machaca las tijeras")
            puntos[0]=puntos[0]+1;puntos[1]=puntos[1]+1
        if Tu==("tijera") and Comp==("piedra"):
            print("PERDISTE: La piedra machaca las tijeras")
            puntos[0]=puntos[0]+1;puntos[2]=puntos[2]+1
        if Tu==("tijera") and Comp==("papel"):
            print("GANASTE: Las tijeras cortan el papel")
            puntos[0]=puntos[0]+1;puntos[1]=puntos[1]+1
    else:
        print("EMPATE")
        puntos[0]=puntos[0]+1;puntos[3]=puntos[3]+1
    pickle.dump(puntos,open("marcador.mio","wb"))
    Res=input("¿Desea ver la puntuación actual?: ")#AQUÍ ESCRIBIR "s" PARA "SÍ", "n" PARA "NO" Y "C" PARA PONER A 0 EL MARCADOR
    if Res!=("C"):
        Res=ns(Res)
    else:
        puntos=pickle.load(open("marcador.mio","rb"))#PONER A 0 EL MARCADOR
        puntos[0]=0;puntos[1]=0;puntos[2]=0;puntos[3]=0
        pickle.dump(puntos,open("marcador.mio","wb"))
    if Res==("s"):
        print("PARTIDAS JUGADAS:",puntos[0],"GANADAS:",puntos[1],"PERDIDAS:",puntos[2],"EMPATES:",puntos[3])
    conti=ns(input("¿Jugar otra vez?: "))
    if conti==("n"):
        break
    else:
        try:
            subprocess.call(["cmd.exe","/C","cls"])
        except:
            continue



