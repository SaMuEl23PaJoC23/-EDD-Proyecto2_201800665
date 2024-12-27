from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
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
        
        print(">>> datos Rutas:")
        for ruta in rutas:#todo: ACA SE INSERTARIAN LOS DATOS A LISTA SIMPLE, lista adyacencia
            print(ruta)
            print("=============================================")
        
        mostrar_botones()
        graphMapa(rutas)

#-----------------------------------------------------------------------
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

        print(">>> Datos Clientes:")
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

#--------ventana Clientes------------------------------------------------
def AbrirVentanaClientes():
    mainWindow.withdraw() #Oculta la ventana principal
    ClientesWindow = Toplevel(mainWindow)
    ClientesWindow.title("- Clientes -")
    ClientesWindow.geometry("480x370")
    ClientesWindow.config(bg="green")
    ClientesWindow.grab_set() #bloquea la interaccion con la ventana anterior
    centrarVentana(ClientesWindow)

    def on_close():
        ClientesWindow.grab_release() #Libera el bloqueo de eventos
        ClientesWindow.destroy()
        mainWindow.deiconify() #Muestra nuevamente la ventana principal
    
    ClientesWindow.protocol("WM_DELETE_WINDOW", on_close)
#--------Funciones ventana Clientes------------------------------------------------
    def BloqueoCamposClientes():
        dpi_.config(state='disabled')
        nombres_.config(state='disabled')
        apellidos_.config(state='disabled')
        genero_.config(state='disabled')
        telefono_.config(state='disabled')
        direccion_.config(state='disabled')

    def DesbloqueoCamposClientes():
        dpi_.config(state='normal')
        nombres_.config(state='normal')
        apellidos_.config(state='normal')
        genero_.config(state='normal')
        telefono_.config(state='normal')
        direccion_.config(state='normal')

    def seleccionDPI(event):
        seleccion_dpi = combxDPIclientes.get()
        print(seleccion_dpi)

    def agregarCliente():
        DesbloqueoCamposClientes()
        messagebox.showwarning("Advertencia", "Ya puede ingresar datos!")
        btnGuardar_clientes.place(x=320, y=260)

    def GuardarEnClientes():
        if(dpi_.get()!="" and nombres_.get() !="" and apellidos_.get() !="" and genero_ !="" and telefono_.get() !="" and direccion_.get() !=""):
            print("guarda el dato")
            btnGuardar_clientes.place_forget() #Permite ocultar boton
            messagebox.showinfo("Atencion", "Datos guardado")
            dpi_.insert(0,"")   #Limpia la entrada
            nombres_.insert(0,"")
            apellidos_.insert(0,"")
            genero_.insert(0,"")
            telefono_.insert(0,"")
            direccion_.insert(0,"")
        else:
            messagebox.showerror("Alerta","Campo(s) vacio(s)...")
#--------Cuerpo Ventana Clientes---------------------------------------------------
    btnCargaClientes = Button(ClientesWindow, text="Carga Masiva", bg="orange", command=cargaArchivoClientes)
    btnCargaClientes.place(x=20, y=5)

    listaDPI=[142,456, 112, 456, 789, 101]  #<<<<< lista temporal
    combxDPIclientes = ttk.Combobox(ClientesWindow, values=listaDPI)
    combxDPIclientes.place(x=300, y=15)
    combxDPIclientes.bind("<<ComboboxSelected>>", seleccionDPI)

    btnAgregarCliente = Button(ClientesWindow, text="Agregar", bg="cyan", command=agregarCliente)
    btnAgregarCliente.place(x=30, y=55)

    btnEditarCliente = Button(ClientesWindow, text="Editar", bg="cyan")
    btnEditarCliente.place(x=35, y=105)
    btnEditarCliente.config(state='disabled')
    
    btnEliminarCliente = Button(ClientesWindow, text="Eliminar", bg="cyan")
    btnEliminarCliente.place(x=200, y=55)
    btnEliminarCliente.config(state='disabled')

    btnVerClientesEstruct = Button(ClientesWindow, text="Mostrar Estructura", bg="cyan")
    btnVerClientesEstruct.place(x=170, y=105)
    btnVerClientesEstruct.config(state='disabled')

    btnGuardar_clientes = Button(ClientesWindow, text="Guardar", bg="red", command=GuardarEnClientes)

    lbDPI = Label(ClientesWindow, text="DPI: ", bg="lightgreen")
    lbDPI.place(x=50, y=155)
    dpi_ = Entry(ClientesWindow)
    dpi_.place(x=90,y=155)
    
    lbNombre = Label(ClientesWindow, text="Nombres: ", bg="lightgreen")
    lbNombre.place(x=20, y=190)
    nombres_ = Entry(ClientesWindow)
    nombres_.place(x=90,y=190)

    lbApellidos = Label(ClientesWindow, text="Apellidos: ", bg="lightgreen")
    lbApellidos.place(x=20, y=225)
    apellidos_ = Entry(ClientesWindow)
    apellidos_.place(x=90,y=225)

    lbGenero = Label(ClientesWindow, text="Genero: ", bg="lightgreen")
    lbGenero.place(x=30, y=260)
    genero_ = Entry(ClientesWindow)
    genero_.place(x=90,y=260)

    lbTelefono = Label(ClientesWindow, text="Telefono: ", bg="lightgreen")
    lbTelefono.place(x=20, y=300)
    telefono_ = Entry(ClientesWindow)
    telefono_.place(x=90,y=300)

    lbDireccion = Label(ClientesWindow, text="Direccion: ", bg="lightgreen")
    lbDireccion.place(x=20, y=335)
    direccion_ = Entry(ClientesWindow)
    direccion_.place(x=90,y=335)
    BloqueoCamposClientes()

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
#btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=cargaArchivoMapa) PARA FUNCIONAMIENTO NORMAL, REMOVER ESTA LINEA
btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=AbrirVentanaClientes)
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