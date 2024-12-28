from nodoCircular import NodoCircular

class CircularDoble():

    def __init__(self):
        self.__largo = 0
        self.__primero = None

    # Con ordenamiento de menor a mayor
    def agregarEnCircular(self, dpi, nombres, apellidos, genero, telefono, direccion):
        nuevo = NodoCircular(dpi, nombres, apellidos, genero, telefono, direccion)
        temp = None

        if(self.__primero != None):
            temp = self.__primero

            if(self.__largo == 1):
                temp.setDrchaCircular(nuevo)
                temp.setIzqCircular(nuevo)

                nuevo.setDrchaCircular(temp)
                nuevo.setIzqCircular(temp)

                #Unicamente se actualiza el puntero primero si el dato nuevo es menor al actual primero
                if(nuevo.getDPI() < temp.getDPI()):
                    self.__primero = nuevo
                    
            
            elif(self.__largo > 1):
                if(nuevo.getDPI() < temp.getDPI()):
                    nuevo.setDrchaCircular(temp)
                    nuevo.setIzqCircular(temp.getIzqCircular())

                    temp.getIzqCircular().setDrchaCircular(nuevo)
                    temp.setIzqCircular(nuevo)

                    #Unicamente se actualiza el puntero primero si el dato nuevo es menor al actual primero
                    self.__primero = nuevo

                else:
                    temp = temp.getDrchaCircular()
                    while (temp != self.__primero):
                        if(nuevo.getDPI() < temp.getDPI()):
                            nuevo.setDrchaCircular(temp)
                            nuevo.setIzqCircular(temp.getIzqCircular())

                            temp.getIzqCircular().setDrchaCircular(nuevo)
                            temp.setIzqCircular(nuevo)
                            break

                        temp = temp.getDrchaCircular()

                    if(temp == self.__primero):
                        temp = temp.getIzqCircular()

                        nuevo.setIzqCircular(temp)
                        nuevo.setDrchaCircular(self.__primero)
                        temp.setDrchaCircular(nuevo)
                        self.__primero.setIzqCircular(nuevo)


        else:
            nuevo.setDrchaCircular(nuevo)
            nuevo.setIzqCircular(nuevo)
            self.__primero = nuevo

        self.__largo += 1

    #----------------------------------------------------------
    def existenteEnCircular(self, dpi):
        if(self.__primero != None):
            temp = self.__primero
            
            while True:
                if(dpi == temp.getDPI()):   #si el dato existe, devuelve True
                    return True
                temp = temp.getDrchaCircular()
                if(temp == self.__primero): #Si el dato no existe, dado que volvio a puntero primero, devuelve False
                    return False
        
        else:
            return False
        
    #----------------------------------------------------------
    def eliminarEnCircular(self, dpi):
        if(self.__primero != None):
            temp = self.__primero
            if(self.__largo == 1):
                if(dpi == temp.getDPI()):
                    aux = temp
                    del aux
                    self.__primero = None
                    self.__largo = 0
                else:
                    print("Valor no existente en lista Circular...")

            elif(self.__largo > 1):
                while True:
                    if(dpi == temp.getDPI()):
                        temp.getDrchaCircular().setIzqCircular(temp.getIzqCircular())
                        temp.getIzqCircular().setDrchaCircular(temp.getDrchaCircular())
                        if(temp == self.__primero): #si el nodo a eliminar es el primero, pero hay mas nodos, se mueve el puntero primero
                            self.__primero = temp.getDrchaCircular()
                        del temp
                        self.__largo -= 1
                        break

                    temp = temp.getDrchaCircular()
                    if(temp == self.__primero):
                        print("Valor no existente en lista Circular...")
                        break

        else:
            print("Lista Vacia!")
    #----------------------------------------------------------
    def getDatosCliente(self, dpi):
        if(self.__primero != None):
            temp = self.__primero
            while True:
                if(dpi == temp.getDPI()):
                    return temp #Si encuentra DATO, lo devuelve
                temp = temp.getDrchaCircular()
                if(temp == self.__primero):
                    break
        
        print("No hay datos que coincida...")
        return None

    #----------------------------------------------------------
    def dpiComboBox(self):
        if(self.__primero != None):
            temp = self.__primero
            DPIlista = []

            while True:
                DPIlista.append(temp.getDPI())
                temp = temp.getDrchaCircular()
                if(temp == self.__primero):
                    break
            return DPIlista

        else:
            print("No hay nada para ComboBox...")
            return []

    #----------------------------------------------------------
    def ImprimirCircular(self):
        if(self.__primero != None):
            temp = self.__primero

            print("======= NUEVA ITERACION =======")
            while True:
                print("DPI:"+str(temp.getDPI()))
                print("Nombres: "+temp.getNombres())
                print("Apellidos: "+temp.getApellidos())
                print("Genero: "+temp.getGenero())
                print("telefono: "+temp.getTelefono())
                print("Direccion: "+temp.getDireccion())
                print("---------------------------------------")
                temp = temp.getDrchaCircular()

                if(temp == self.__primero):
                    break
        else:
            print("No hay nada que mostrar...")