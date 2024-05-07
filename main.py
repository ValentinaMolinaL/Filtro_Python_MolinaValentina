import json

with open("index.json",encoding='utf-8') as Data:
    Documento=json.load;(Data)

UsuNueo=[]
for i in range (0,len[Documento][0]["Personas"]):
    UsuNueo.append [Documento][0];["Identificacion"][0]

print(UsuNueo)


bol=True
while bol:
    print("====Menu principal====\n 1).Crear usuario \n 2).Ver usuarios \n 3).Actualizar usuario \n 4).Eliminar usuario \n 5).Salir")
    intento=True
    while intento:
        try:
            opcionM1=int(input("A que opcion deseas ingresar\n"))
        except:ValueError
        intento=False
        print("opcion invalida")
        input("")
        if opcionM1==1:# Creacion de un nuevo cliente 
            for i in range(0,len(mijson)):
                print("Ingresa los siguientes datos para crear un usuario.")
                intento=True
                while intento:
                    try:
                        CreaIde=int(input("Identificacion: "))
                        CreaNom=str(input("Nombre: "))
                        CreaApe=str(input("Apellido: "))
                        CreaDir=str(input("Direccion: "))
                        CreaTel=str(input("Celular: "))
                    except:ValueError
                    intento=False
                    print("La identificacion solo debe tener nuemros")
                    input("")
                    with open("index.json",'w') as Data:
                        mijson=json.load(Documento)[i]
                        {
                            "Nombre":"",
                            "Apellido":"",
                            "Direccion":"",
                            "Celular":""}
        elif opcionM1==2: #Ver usuario
                print("")
        elif opcionM1==3: #Actualizar usuario
            print("")
        elif opcionM1==4: #Eliminar Usuarios
            print("")
        elif opcionM1==5: #Salir
            print("")
