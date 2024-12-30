from nodoSimple import NodoSimple
from graphviz import Digraph

class ListaSimple():
    
    def __init__(self):
        self.__primero = None

    #----------------------------------------------------------
    def agregarEnSimple(self, IDviaje, lugarOrigen, lugarDestino, fecha, hora):
        nuevo = NodoSimple(IDviaje, lugarOrigen, lugarDestino, fecha, hora)
        temp = None

        if(self.__primero == None):
            self.__primero = nuevo

        else:
            temp = self.__primero
            while(temp.getSig() != None):
                temp = temp.getSig()

            temp.setSig(nuevo)
    #----------------------------------------------------------
    def existenteEnSimple(self, IDviaje):
        if(self.__primero != None):
            temp = self.__primero

            while(temp != None):
                if(IDviaje == temp.getIDviaje()):
                    return True
                temp = temp.getSig()

            return False

        else:
            return False
    #----------------------------------------------------------
    def getDatosViaje(self, IDviaje):
        if(self.__primero != None):
            temp = self.__primero

            while(temp != None):
                if(IDviaje == temp.getIDviaje()):
                    return temp
                temp = temp.getSig()

            return []

        else:
            return []
    #----------------------------------------------------------
    def idViajesComboBox(self):
        if(self.__primero != None):
            temp = self.__primero
            IDviajes = []

            while(temp != None):
                IDviajes.append(temp.getIDviaje())
                temp = temp.getSig()

            return IDviajes

        else:
            print("No hay nada para ComboBox Viajes...")
            return []
    #----------------------------------------------------------
    def ImprimirSimple(self):
        if(self.__primero != None):
            temp = self.__primero

            while(temp != None):
                print("ID: "+temp.getIDviaje())
                print("Origen: "+temp.getLugarOrigen())
                print("Destino: "+temp.getLugarDestino())
                print("Fecha: "+temp.getFecha())
                print("Hora: "+temp.getHora()+"\n")

                temp = temp.getSig()

        else:
            print("No hay nada que mostrar...")
    #----------------------------------------------------------
    def graficarViaje(self, IDviaje):
        if(self.__primero != None):
            temp = self.__primero
            while(IDviaje != temp.getIDviaje()):
                temp = temp.getSig()

            #creacion de grafo dirigido
            dot = Digraph(name='ListaSimpleViaje', graph_attr={'rankdir': 'LR'})

            #Creacion nodo
            dot.node(temp.getLugarOrigen(), label='< <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>'+temp.getLugarOrigen()+'</TD></TR> <TR><TD>'+temp.getFecha()+'</TD></TR> <TR><TD>'+temp.getHora()+'</TD></TR>  </TABLE> >', shape='circle', style='filled', fillcolor='lightgreen')

            #Creacion enlace
            dot.edge(temp.getLugarOrigen(), temp.getLugarDestino())

            #Guarda y renderiza el grafico
            dot.render('Graph_simpleViaje', format='png', view=True)

        else:
            print("Lista Simple Vacia, no Graficar!")
    #----------------------------------------------------------
    def graficarViajes(self):
        if(self.__primero != None):
            temp = self.__primero

            #creacion de grafo dirigido
            dot = Digraph(name='ListaViajes', graph_attr={'rankdir': 'LR'})
            while(temp != None):
                #Creacion nodo
                dot.node(temp.getIDviaje(), label='< <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"><TR><TD>'+temp.getIDviaje()+'</TD></TR> <TR><TD>'+temp.getLugarOrigen()+'</TD></TR> <TR><TD>'+temp.getLugarDestino()+'</TD></TR> <TR><TD>'+temp.getFecha()+'</TD></TR> <TR><TD>'+temp.getHora()+'</TD></TR>  </TABLE> >', shape='circle', style='filled', fillcolor='lightgreen')

                #Creacion enlace
                if(temp.getSig() != None):
                    dot.edge(temp.getIDviaje(), temp.getSig().getIDviaje())

                temp = temp.getSig()

            #Guarda y renderiza el grafico
            dot.render('Graph_Viajes', format='png', view=True)

        else:
            print("Lista Simple Vacia, no Graficar Estructura!")