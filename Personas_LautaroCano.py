class Persona():

    def __init__(self,pNombre,pSNombre,pApellido,pSApellido,pDNI,pDireccion,pTelefono,pEscuelas):
        self.Nombre = pNombre
        self.SegundoNombre = pSNombre
        self.Apellido = pApellido
        self.SegundoApellido = pSApellido
        self.DNI = pDNI
        self.Direccion = pDireccion
        self.Telefono = pTelefono
        self.Escuelas = pEscuelas


    def VerNombre(self):
        return self.Nombre
    def VerSNombre(self):
        return self.SegundoNombre
    def VerApellido(self):
        return self.Apellido
    def VerSApellido(self):
        return self.SegundoApellido
    def VerDNI(self):
        return self.DNI
    def VerDireccion(self):
        return self.Direccion
    def VerTelefono(self):
        return self.Telefono
    def VerEscuelas(self):
        return self.Escuelas

    def ModificarNombre(self,nNombre):  #n = Nuevo
        self.Nombre = nNombre
    def ModificarSNombre(self,nSNombre):
        self.SegundoNombre = nSNombre  #s = Segundo
    def ModificarApellido(self,nApellido):
        self.Apellido = nApellido
    def ModificarSApellido(self,nSApellido):
        self.SegundoApellido = nSApellido
    def ModificarDireccion(self,nDireccion):
        self.Direccion = nDireccion
    def ModificarTelefono(self,nTelefono):
        self.Telefono = nTelefono
    def ModificarEscuelas(self,nEscuelas):
        self.Escuelas = nEscuelas

#main
menu=9
menu2=9
menu3=9
menu4=9
menu5=9
menu6=9
menu7=9
i=0     #Posicion de los nombres etc en listas
listaPersona=[] * 100
v=0     #Variable para Menu
bdni=0  #Buscar DNI, Variable con la posicion del DNI en la lista
buscar = 0

while menu != 5:
    print("\n\n          MENU")
    print("\n1-Ingresar datos")
    print("2-Consultar sus datos")
    print("3-Dar de baja sus datos")
    print("4-Modificar sus datos")
    print("5-Salir del programa")
    menu = int(input("Opción:"))

    menu2= menu2 + 9
    menu4=menu4 + 9
    menu5=menu5 + 9
    menu6=menu6 + 9

    if(menu==1): # INGRESO DATOS
        print("\n       INGRESO DATOS")

        pnombre=input("\nIngrese Nombre:")
        while pnombre.isalpha() == False:
            pnombre.isalpha()
            print("Ingrese un nombre valido.")
            pnombre=input("\nIngrese Nombre:")


        print("\nQuiere ingresar segundo nombre?")
        print("\n1-Si")
        print("2-No")
        v = int(input(":"))
        if(v==1):
            psnombre=input("\nIngrese segundo nombre:")
            while psnombre.isalpha() == False:
                psnombre.isalpha()
                print("Ingrese un nombre valido.")
                psnombre=input("\nIngrese segundo nombre:")
            v= v-1
        if(v==2):
            psnombre=1

        papellido=input("\nIngrese Apellido:")
        while papellido.isalpha() == False:
            papellido.isalpha()
            print("Ingrese un apellido valido.")
            papellido=input("\nIngrese Apellido:")

        print("\nQuiere ingresar segundo apellido?")
        print("\n1-Si")
        print("2-No")
        v = int(input(":"))
        if(v==1):
            psapellido=input("\nIngrese segundo apellido:")
            while psapellido.isalpha() == False:
                psapellido.isalpha()
                print("Ingrese un apellido valido.")
                psapellido=input("\nIngrese Apellido:")
            v= v-1
        if(v==2):
            psapellido=1

        while True:
            try:
                print("\nIngrese DNI sin puntos ni comas.")
                pdni = int(input("Ingrese DNI:"))
                print("")
                break
            except ValueError:
                print("\nIngrese un DNI valido.")

        pdireccion=input("\nIngrese direccion:")

        while True:
            try:
                ptelefono=int(input("\nIngrese telefono:"))
                break
            except ValueError:
                print("Ingrese un telefono valido.")

        pescuelas=input("\nIngrese Escuelas(Separados por /):")

        listaPersona.append(Persona(pnombre,psnombre,papellido,psapellido,pdni,pdireccion,ptelefono,pescuelas)) #p = Persona
        i = i + 1
    if(menu==2): # CONSULTAR DATOS
        while(menu2!=5):
            print("\n      CONSULTAR DATOS")
            print("\n\n1-Ingresar DNI")
            print("5-Volver menu anterior")
            menu2 = int(input("Opción:"))
            if(menu2==1):
                while True:
                    try:
                        print("\nIngrese DNI sin puntos ni comas.")
                        bdni= int(input("DNI:")) #bdni= DNI
                        print("")
                        break
                    except ValueError:
                        print("\nIngrese un DNI valido.")
                for b in range(len(listaPersona)): #Recorre la lista
                    if bdni == listaPersona[b].DNI:# Buscar Posicion
                        buscar=b #Guarda el index en el que coincidio el DNI
                        print("\n              DATOS DEL USUARIO:")
                        print(f"      Nombre= {listaPersona[buscar].VerNombre()}")
                        if(listaPersona[buscar].SegundoNombre !=1):
                            print(f"      Segundo Nombre= {listaPersona[buscar].VerSNombre()}")
                        print(f"      Apellido= {listaPersona[buscar].VerApellido()}")
                        if(listaPersona[buscar].SegundoApellido !=1):
                            print(f"      SegundoApellido= {listaPersona[buscar].VerSApellido()}")
                        print(f"      DNI= {listaPersona[buscar].VerDNI()}")
                        print(f"      Direccion= {listaPersona[buscar].VerDireccion()}")
                        print(f"      Telefono= {listaPersona[buscar].VerTelefono()}")
                        print(f"      Escuelas= {listaPersona[buscar].VerEscuelas()}")
                    else:
                        print("No se encontró ese usuario.")
                        menu2=9  #Vuelve al menu Consultar datos
    if(menu==3): # DAR DE BAJA DATOS
        while(menu4!=5):
            print("\n      DAR DE BAJA DATOS")

            print("\n1-Ingresar DNI")
            print("5-Volver menu anterior")
            menu4 = int(input("Opción:"))
            if(menu4==1):
                while True:
                    try:
                        print("\nIngrese DNI sin puntos ni comas.")
                        bdni= int(input("DNI:"))
                        print("")
                        break
                    except ValueError:
                        print("\nIngrese un DNI valido.")
                for b in range(len(listaPersona)):
                    buscar=0
                    if bdni == listaPersona[b].DNI:# Buscar Posicion
                        buscar=b
                        print("\n              EL USUARIO:")
                        print(f"      Nombre= {listaPersona[buscar].VerNombre()}")
                        if(listaPersona[buscar].SegundoNombre !=1):
                            print(f"      Segundo Nombre= {listaPersona[buscar].VerSNombre()}")
                        print(f"      Apellido= {listaPersona[buscar].VerApellido()}")
                        if(listaPersona[buscar].SegundoApellido !=1):
                            print(f"      SegundoApellido= {listaPersona[buscar].VerSApellido()}")
                        print(f"      DNI= {listaPersona[buscar].VerDNI()}")
                        print(f"      Direccion= {listaPersona[buscar].VerDireccion()}")
                        print(f"      Telefono= {listaPersona[buscar].VerTelefono()}")
                        print(f"      Escuelas= {listaPersona[buscar].VerEscuelas()}")
                        print("\n              Fue dado de baja.")
                        listaPersona.pop(buscar)
                    else:
                        print("No se encontró ese usuario.")
                menu4=5
                menu= 9
    if(menu==4): # MODIFICAR DATOS
        while(menu5!=5):
            print("\n      MODIFICAR DATOS")
            menu6= menu6 + 9
            while True:
                try:
                    print("\nIngrese DNI sin puntos ni comas.")
                    bdni= int(input("DNI:")) #bdni= DNI
                    print("")
                    break
                except ValueError:
                    print("\nIngrese un DNI válido.")
            for b in range(len(listaPersona)):
                buscar=0
                if bdni == listaPersona[b].DNI:# Buscar Posicion
                    buscar=b
                    while(menu6!=7):
                        print(f"\n        Que desea modificar {listaPersona[buscar].VerNombre()} {listaPersona[buscar].VerApellido()}?")
                        print("\n1-Modificar todos sus datos.")
                        print("2-Modificar DNI.")
                        print("3-Nombre/s.")
                        print("4-Apellido/s.")
                        print("5-Contacto")
                        print("7-Menu Anterior.")
                        menu6 = int(input("Opción:"))
                        menu7 = menu7 + 9
                        if(menu6==1):
                            x=0
                            nNombre=input("\nIngrese Nombre:")
                            while nNombre.isalpha() == False:
                                nNombre.isalpha()
                                print("Ingrese un nombre válido.")
                                nNombre = input("\nIngrese Nombre:")
                            listaPersona[buscar].ModificarNombre(nNombre)

                            nSNombre=''
                            if(listaPersona[buscar].SegundoNombre!=1):
                                nSNombre= input("\nIngrese segundo Nombre:")
                                while nSNombre.isalpha() == False:
                                    nSNombre.isalpha()
                                    print("Ingrese un nombre válido.")
                                    nSNombre= input("\nIngrese segundo Nombre:")
                                listaPersona[buscar].ModificarSNombre(nSNombre)

                            nApellido = input("\nIngrese Apellido:")
                            while nApellido.isalpha() == False:
                                nApellido.isalpha()
                                print("Ingrese un apellido valido.")
                                nApellido = input("\nIngrese Apellido:")
                            listaPersona[buscar].ModificarApellido(nApellido)
                            nSApellido=''
                            if(listaPersona[buscar].SegundoApellido!=1):
                                while nSApellido.isalpha() == False:
                                    nSApellido.isalpha()
                                    print("Ingrese un apellido válido.")
                                    nSApellido = input("\nIngrese segundo apellido:")
                                listaPersona[buscar].ModificarSApellido(nSApellido)

                            nDireccion = input("\nIngresar Direccion:")
                            listaPersona[buscar].ModificarDireccion(nDireccion)

                            while True:
                                try:
                                    nTelefono = int(input("\nIngrese teléfono:"))
                                    break
                                except ValueError:
                                    print("Ingrese un teléfono válido.")
                            listaPersona[buscar].ModificarTelefono(nTelefono)

                            nEscuelas =input("\nIngrese Escuelas(Separados por /):")
                            listaPersona[buscar].ModificarEscuelas(nEscuelas)
                            menu6=9
                        if(menu6==2):
                            while(menu7!=5):
                                print("\n      Dar de baja DNI con todos los datos.")

                                print("\n1-Ingresar DNI")
                                print("5-Volver menu anterior")
                                menu7 = int(input("Opción:"))
                                if(menu7==1):
                                    while True:
                                        try:
                                            print("\nIngrese DNI sin puntos ni comas.")
                                            bdni= int(input("DNI:"))
                                            print("")
                                            break
                                        except ValueError:
                                            print("\nIngrese un DNI valido.")
                                    for b in range(len(listaPersona)):
                                        buscar=0
                                        if bdni == listaPersona[b].DNI:# Buscar Posicion
                                            buscar=b
                                            print("\n              EL USUARIO:")
                                            print(f"      Nombre= {listaPersona[buscar].VerNombre()}")
                                            if(listaPersona[buscar].SegundoNombre !=1):
                                                print(f"      Segundo Nombre= {listaPersona[buscar].VerSNombre()}")
                                            print(f"      Apellido= {listaPersona[buscar].VerApellido()}")
                                            if(listaPersona[buscar].SegundoApellido !=1):
                                                print(f"      SegundoApellido= {listaPersona[buscar].VerSApellido()}")
                                            print(f"      DNI= {listaPersona[buscar].VerDNI()}")
                                            print(f"      Direccion= {listaPersona[buscar].VerDireccion()}")
                                            print(f"      Telefono= {listaPersona[buscar].VerTelefono()}")
                                            print(f"      Escuelas= {listaPersona[buscar].VerEscuelas()}")
                                            print("\n              Fue dado de baja.")
                                            listaPersona.pop(buscar)
                                        else:
                                            print("No se encontró ese usuario.")
                        if(menu6==3):
                            nNombre=input("\nIngrese Nombre:")
                            while nNombre.isalpha() == False:
                                nNombre.isalpha()
                                print("Ingrese un nombre valido.")
                                nNombre = input("\nIngrese Nombre:")
                            listaPersona[buscar].ModificarNombre(nNombre)

                            nSNombre=''
                            if(listaPersona[buscar].SegundoNombre!=1):
                                nSNombre= input("\nIngrese segundo Nombre:")
                                while nSNombre.isalpha() == False:
                                    nSNombre.isalpha()
                                    print("Ingrese un nombre valido.")
                                    nSNombre= input("\nIngrese segundo Nombre:")
                                listaPersona[buscar].ModificarSNombre(nSNombre)
                        if(menu6==4):
                            nApellido = input("\nIngrese Apellido:")
                            while nApellido.isalpha() == False:
                                nApellido.isalpha()
                                print("Ingrese un apellido valido.")
                                nApellido = input("\nIngrese Apellido:")
                            listaPersona[buscar].ModificarApellido(nApellido)

                            nSApellido=''
                            if(listaPersona[buscar].SegundoApellido!=1):
                                while nSApellido.isalpha() == False:
                                    nSApellido.isalpha()
                                    print("Ingrese un apellido valido.")
                                    nSApellido = input("\nIngrese segundo apellido:")
                                listaPersona[buscar].ModificarSApellido(nSApellido)
                        if(menu6==5):
                            nDireccion = input("\nIngresar Direccion:")
                            listaPersona[buscar].ModificarDireccion(nDireccion)

                            while True:
                                try:
                                    nTelefono = int(input("\nIngrese telefono:"))
                                    break
                                except ValueError:
                                    print("Ingrese un telefono valido.")
                            listaPersona[buscar].ModificarTelefono(nTelefono)

                            nEscuelas =input("\nIngrese Escuelas(Separados por /):")
                            listaPersona[buscar].ModificarEscuelas(nEscuelas)
                        menu5 = 5
                else:
                    print("No existe ese usuario.")
                    menu5=5
