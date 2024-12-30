class NodoSimple():
    
    def __init__(self, IDviaje, lugarOrigen, lugarDestino, fecha, hora):
        self.__IDviaje = IDviaje
        self.__lugarOrigen = lugarOrigen
        self.__lugarDestino = lugarDestino
        self.__fecha = fecha
        self.__hora = hora
        self.__sig = None

    #Getters
    def getIDviaje(self):
        return self.__IDviaje
    
    def getLugarOrigen(self):
        return self.__lugarOrigen
    
    def getLugarDestino(self):
        return self.__lugarDestino
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getSig(self):
        return self.__sig

    #Setters
    def setIDviaje(self, IDviaje):
        self.__IDviaje = IDviaje

    def setLugarOrigen(self, lugarOrigen):
        self.__lugarOrigen = lugarOrigen

    def setLugarDestino(self, lugarDestino):
        self.__lugarDestino = lugarDestino

    def setFecha(self, fecha):
        self.__fecha = fecha

    def setHora(self, hora):
        self.__hora = hora

    def setSig(self, siguiente):
        self.__sig = siguiente