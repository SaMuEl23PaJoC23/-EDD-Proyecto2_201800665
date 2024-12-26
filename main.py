from tkinter import *
from tkinter import filedialog
from io import open
from PIL import Image, ImageTk
from graphviz import Graph
#-----------------------------------------------------------------------
def centrarVentana(ventana):
    ventana.update_idletasks()#actualiza la interfaz grafica y procesa cualquier tarea pendiente que este en la cola de eventos
    #Para mostrar ventana principal en el centro:
    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()

    # Calcular la posición (X , Y) para centrar la ventana
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Establecer el tamaño y la posición de la ventana
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

#-----------------------------------------------------------------------
def cargaArchivoMapa():
    rutaArchivoMapa = filedialog.askopenfilename(initialdir="C:\\Users\\samal\\Desktop\\estructuas proyecto PYTHON") 
    if(rutaArchivoMapa != ""):
        archivoRutas = open(rutaArchivoMapa,"r")
        textoRutas = archivoRutas.readlines()
        archivoRutas.close()

        datosRuta=[]
        rutas=[]
        for linea in textoRutas: #Se separan y almacenan las propiedades de cada Ruta
            datosRuta = linea.split('/')
            rutas.append(datosRuta)

        for ruta in rutas: #se remueve '%' y '\n'
            ruta[2] = ruta[2].replace('%','')
            ruta[2] = ruta[2].replace('\n','')
        
        print("datos Rutas:")
        for ruta in rutas:#todo: ACA SE INSERTARIAN LOS DATOS A LISTA SIMPLE, lista adyacencia
            print(ruta)
            print("=============================================")
        
        mostrar_botones()
        graphMapa(rutas)

def cargaArchivoClientes():
    rutaArchivoClientes = filedialog.askopenfilename(initialdir="C:\\Users\\samal\\Desktop\\estructuas proyecto PYTHON") 
    if(rutaArchivoClientes != ""):
        archivoClientes = open(rutaArchivoClientes,"r")
        textoClientes = archivoClientes.readlines()
        archivoClientes.close()

        datosCliente=[]
        clientes=[]
        for linea in textoClientes: #Se separan y almacenan las propiedades de cada Cliente
            datosCliente = linea.split(',')
            clientes.append(datosCliente)

        print("Datos Clientes:")
        for cliente in clientes: #se remueve ';' y '\n'
            cliente[5] = cliente[5].replace(';','')
            cliente[5] = cliente[5].replace('\n','')

        for cliente in clientes:#todo: ACA SE INSERTARIAN LOS DATOS A LISTA CIRCULAR
            print(cliente)
            print("=============================================")

#-----------------------------------------------------------------------
def graphMapa(rutas):
    dot = Graph(engine='fdp')
    nodosExistentes=[]
    
    #Creacion nodos
    for ruta in rutas:
        if(ruta[0] not in nodosExistentes):
            # .node(nombreNodo, etiquetaNodo, ...)
            dot.node(ruta[0], ruta[0], shape='circle', style='filled', color='lightgreen')
            nodosExistentes.append(ruta[0])
        
        if(ruta[1] not in nodosExistentes):
            dot.node(ruta[1], ruta[1], shape='circle', style='filled', color='lightgreen')
            nodosExistentes.append(ruta[1])

    # Agregar aristas (conexiones) entre nodos con etiquetas (distancias)
    for ruta in rutas:
        dot.edge(ruta[0], ruta[1], label=ruta[2])

    dot.render('grafoRutasMapa', format='png')
    actualizarMapa()

#-----------------------------------------------------------------------
def actualizarMapa():
    imagenMapa = Image.open("grafoRutasMapa.png")
    nuevoSizeMapa = imagenMapa.resize((470, 430), Image.LANCZOS)
    paraMapa = ImageTk.PhotoImage(nuevoSizeMapa)
    lbMapa.config(image=paraMapa)
    lbMapa.image = paraMapa # Guarda una referencia para evitar que imagen sea recolectada por el garbage collector    

#-----------------------------------------------------------------------
def mostrar_botones():
    btnClientes.place(x=25, y=12)
    btnVehiculos.place(x=400, y=12)
    btnViajes.place(x=31, y=62)
    btnRutas.place(x=412, y=62)
    btnReportes.place(x=220, y=105)
    btnCargaMapa.place_forget() #Permite ocultar boton

#--------Ajustes ventana Clientes------------------------------------------------
def AbrirVentanaClientes():
    mainWindow.withdraw() #Oculta la ventana principal
    ClientesWindow = Toplevel(mainWindow)
    ClientesWindow.title("- Clientes -")
    ClientesWindow.geometry("500x500")
    ClientesWindow.config(bg="green")
    ClientesWindow.grab_set() #bloquea la interaccion con la ventana anterior
    centrarVentana(ClientesWindow)

    def on_close():
        ClientesWindow.grab_release() #Libera el bloqueo de eventos
        ClientesWindow.destroy()
        mainWindow.deiconify() #Muestra nuevamente la ventana principal
    
    ClientesWindow.protocol("WM_DELETE_WINDOW", on_close)

#-----------------------------------------------------------------------
#----------------------Ajustes ventana main-------------------------------------
mainWindow = Tk()
mainWindow.title("LLEGA RAPIDITO")
mainWindow.geometry("500x600")
mainWindow.config(bg='orange')
centrarVentana(mainWindow)
mainWindow.resizable(False, False)#Hace que no sea Redimensionable
#--------------------------------------------------------------------------------
#-------CUERPO - MAIN -----------------------------------------------------------
btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=cargaArchivoMapa)
btnCargaMapa.place(x=223, y=40)

btnClientes = Button(mainWindow, text="Clientes", bg="darkgreen", fg="white", command=AbrirVentanaClientes)

btnVehiculos = Button(mainWindow, text="Vehiculos", bg="darkgreen", fg="white", command=AbrirVentanaClientes)

btnViajes = Button(mainWindow, text="Viajes", bg="darkgreen", fg="white", command=AbrirVentanaClientes)

btnRutas = Button(mainWindow, text="Rutas", bg="darkgreen", fg="white", command=AbrirVentanaClientes)

btnReportes = Button(mainWindow, text="Reportes", bg="black", fg="white", command=AbrirVentanaClientes)

imagenLogo = Image.open("llegaRa.png")
nuevoSizeLogo = imagenLogo.resize((470,430), Image.LANCZOS)
paraMapa = ImageTk.PhotoImage(nuevoSizeLogo)

lbMapa = Label(mainWindow, image=paraMapa)
lbMapa.place(x=10, y=150)

#-----------------------------------------------------------------------
mainWindow.mainloop()