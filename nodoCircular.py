class NodoCircular():
    def __init__(self, dpi, nombres, apellidos, genero, telefono, direccion):
        self.__dpi = dpi
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__genero = genero
        self.__telefono = telefono
        self.__direccion = direccion
        self.__drchaCircular = None
        self.__izqCircular = None

    #Getters
    def getDPI(self):
        return self.__dpi
    
    def getNombres(self):
        return self.__nombres
    
    def getApellidos(self):
        return self.__apellidos
    
    def getGenero(self):
        return self.__genero
    
    def getTelefono(self):
        return self.__telefono
    
    def getDireccion(self):
        return self.__direccion
    
    def getDrchaCircular(self):
        return self.__drchaCircular
    
    def getIzqCircular(self):
        return self.__izqCircular

    #Setters
    def setDPI(self, dpi):
        self.__dpi = dpi

    def setNombres(self, nombres):
        self.__nombres = nombres

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setGenero(self, genero):
        self.__genero = genero

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setDrchaCircular(self, drchaCircular):
        self.__drchaCircular = drchaCircular

    def setIzqCircular(self, izqCircular):
        self.__izqCircular = izqCircular