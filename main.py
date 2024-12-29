from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from io import open
from PIL import Image, ImageTk
from graphviz import Graph

from circularDoble import CircularDoble

cd = CircularDoble()
listaDPIcbox = []
#-----------Funciones Ventana Main--------------------------------------
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

def actualizarMapa():
    imagenMapa = Image.open("grafoRutasMapa.png")
    nuevoSizeMapa = imagenMapa.resize((470, 430), Image.LANCZOS)
    paraMapa = ImageTk.PhotoImage(nuevoSizeMapa)
    lbMapa.config(image=paraMapa)
    lbMapa.image = paraMapa # Guarda una referencia para evitar que imagen sea recolectada por el garbage collector    

def mostrar_botones():
    btnClientes.place(x=25, y=12)
    btnVehiculos.place(x=400, y=12)
    btnViajes.place(x=31, y=62)
    btnRutas.place(x=412, y=62)
    btnReportes.place(x=220, y=105)
    btnCargaMapa.place_forget() #Permite ocultar boton

#-----------------------------------------------------------------------
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

            for cliente in clientes: #se remueve ';' y '\n'
                cliente[5] = cliente[5].replace(';','')
                cliente[5] = cliente[5].replace('\n','')

            for cliente in clientes:#Se agregan clientes a lista Circular
                cd.agregarEnCircular(int(cliente[0]), cliente[1], cliente[2], cliente[3], cliente[4], cliente[5])

            actualizaComboBoxDPI()
            cd.ImprimirCircular()
            messagebox.showwarning("Advertencia", "! Clientes Cargados !")

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

    def limpiarCamposClientes():
        dpi_.delete(0, END)   #Limpia la entrada del campo DPI
        nombres_.delete(0, END)
        apellidos_.delete(0, END)
        genero_.delete(0, END)
        telefono_.delete(0, END)
        direccion_.delete(0, END)

    def habilitarOtrasFuncionesClientes():
        lbDPIcBox.place(x=265, y=15)
        combxDPIclientes.place(x=300, y=15) #Muestra ComboBox
        btnEditarCliente.config(state='normal')
        btnEliminarCliente.config(state='normal')
        btnVerClientesEstruct.config(state='normal')

    def desHabilitarOtrasFuncionesCliente():
        lbDPIcBox.place_forget()
        combxDPIclientes.place_forget() #Oculta ComboBox
        btnEditarCliente.config(state='disabled')
        btnEliminarCliente.config(state='disabled')
        btnVerClientesEstruct.config(state='disabled')

    def seleccionDPI(event):
        seleccion_dpi = int(combxDPIclientes.get())   #Seleccion de DPI la toma como str, se debe convertir a int, para comparacion
        DesbloqueoCamposClientes()
        limpiarCamposClientes()
        datosCliente = cd.getDatosCliente(seleccion_dpi)
        dpi_.insert(0, str(datosCliente.getDPI()))
        nombres_.insert(0, datosCliente.getNombres())
        apellidos_.insert(0, datosCliente.getApellidos())
        genero_.insert(0, datosCliente.getGenero())
        telefono_.insert(0, datosCliente.getTelefono())
        direccion_.insert(0, datosCliente.getDireccion())
        BloqueoCamposClientes()

    def agregarCliente():
        DesbloqueoCamposClientes()
        limpiarCamposClientes()
        messagebox.showwarning("Advertencia", "Ya puede ingresar datos!")
        btnGuardar_clientes.place(x=320, y=260) #Muesta boton Guardar
        desHabilitarOtrasFuncionesCliente()

    def actualizaComboBoxDPI():
        global listaDPIcbox
        listaDPIcbox = cd.dpiComboBox()
        combxDPIclientes["values"] = listaDPIcbox
        combxDPIclientes.set('')
        if(listaDPIcbox != []):
            habilitarOtrasFuncionesClientes()
        else:
            desHabilitarOtrasFuncionesCliente()

    def guardarNuevoEnClientes():
        if(dpi_.get()!="" and nombres_.get() !="" and apellidos_.get() !="" and genero_ !="" and telefono_.get() !="" and direccion_.get() !=""):
            if(not cd.existenteEnCircular(int(dpi_.get()))):
                btnGuardar_clientes.place_forget() #Permite ocultar boton
                cd.agregarEnCircular(int(dpi_.get()), nombres_.get(), apellidos_.get(), genero_.get(), telefono_.get(), direccion_.get())
                
                actualizaComboBoxDPI()

                limpiarCamposClientes()
                BloqueoCamposClientes()
                messagebox.showinfo("Atencion", "Datos guardado")    
                cd.ImprimirCircular()
            else:
                dpi_.delete(0, END)
                messagebox.showerror("Alerta","DPI Ya existente...")

        else:
            messagebox.showerror("Alerta","Campo(s) vacio(s)...")

    def guardarEditadoEnClientes():
        if(nombres_.get() !="" and apellidos_.get() !="" and genero_.get() !="" and telefono_.get() !="" and direccion_.get() !=""):
            cd.editarCliente(int(dpi_.get()), nombres_.get(), apellidos_.get(), genero_.get(), telefono_.get(), direccion_.get())

            dpi_.config(state='normal') #se desbloque campo para luego poder ser limpiado
            limpiarCamposClientes()
            BloqueoCamposClientes()
            habilitarOtrasFuncionesClientes()
            combxDPIclientes.set('')
            btnAgregarCliente.config(state='normal')
            btnCargaClientes.config(state='normal')
            cd.ImprimirCircular()
            btnGuardarEditado.place_forget() #Oculta boton
            messagebox.showinfo("Atencion", "Se guardo Datos editados")    

        else:
            messagebox.showerror("Alerta","Campo(s) vacio(s)...")

    def eliminarCliente():
        if(combxDPIclientes.get() != ""):
            cd.eliminarEnCircular(int(combxDPIclientes.get()))
            actualizaComboBoxDPI()
            DesbloqueoCamposClientes()
            limpiarCamposClientes()
            BloqueoCamposClientes()
            print("dato eliminado, restantes: ")
            cd.ImprimirCircular()
            messagebox.showwarning("Advertencia", "Cliente eliminado")
        else:
            messagebox.showerror("Alerta","! Debe seleccionar DPI primero !")

    def editarCliente():
        if(combxDPIclientes.get() != ""):
            DesbloqueoCamposClientes()
            dpi_.config(state='disabled')
            desHabilitarOtrasFuncionesCliente()
            btnAgregarCliente.config(state='disabled')
            btnCargaClientes.config(state='disabled')
            btnGuardarEditado.place(x=320, y=260)

        else:
            messagebox.showerror("Alerta","! Debe seleccionar DPI primero !")

    def generarEstructura():
        cd.graficarCircular()

#--------Cuerpo Ventana Clientes---------------------------------------------------
    btnCargaClientes = Button(ClientesWindow, text="Carga Masiva", bg="orange", command=cargaArchivoClientes)
    btnCargaClientes.place(x=20, y=5)

    lbDPIcBox = Label(ClientesWindow, text="DPI: ", bg="lightblue")
    combxDPIclientes = ttk.Combobox(ClientesWindow, values=listaDPIcbox, state="readonly")
    combxDPIclientes.bind("<<ComboboxSelected>>", seleccionDPI)

    btnAgregarCliente = Button(ClientesWindow, text="Agregar Nuevo", bg="cyan", command=agregarCliente)
    btnAgregarCliente.place(x=30, y=55)

    btnEditarCliente = Button(ClientesWindow, text="Editar", bg="cyan", command=editarCliente)
    btnEditarCliente.place(x=40, y=105)
    btnEditarCliente.config(state='disabled')
    
    btnEliminarCliente = Button(ClientesWindow, text="Eliminar", bg="cyan", command=eliminarCliente)
    btnEliminarCliente.place(x=200, y=55)
    btnEliminarCliente.config(state='disabled')

    btnVerClientesEstruct = Button(ClientesWindow, text="Mostrar Estructura", bg="cyan", command=generarEstructura)
    btnVerClientesEstruct.place(x=170, y=105)
    btnVerClientesEstruct.config(state='disabled')

    if(listaDPIcbox != []):
        habilitarOtrasFuncionesClientes()

    btnGuardar_clientes = Button(ClientesWindow, text="Guardar", bg="red", command=guardarNuevoEnClientes)
    btnGuardarEditado = Button(ClientesWindow, text="Guardar Editado", bg="red", command=guardarEditadoEnClientes)

    lbDPI = Label(ClientesWindow, text="DPI: ", bg="lightgreen")
    lbDPI.place(x=50, y=155)
    dpi_ = Entry(ClientesWindow, width=25)
    dpi_.place(x=90,y=155)
    
    lbNombre = Label(ClientesWindow, text="Nombres: ", bg="lightgreen")
    lbNombre.place(x=20, y=190)
    nombres_ = Entry(ClientesWindow, width=25)
    nombres_.place(x=90,y=190)

    lbApellidos = Label(ClientesWindow, text="Apellidos: ", bg="lightgreen")
    lbApellidos.place(x=20, y=225)
    apellidos_ = Entry(ClientesWindow, width=25)
    apellidos_.place(x=90,y=225)

    lbGenero = Label(ClientesWindow, text="Genero: ", bg="lightgreen")
    lbGenero.place(x=30, y=260)
    genero_ = Entry(ClientesWindow)
    genero_.place(x=90,y=260)

    lbTelefono = Label(ClientesWindow, text="Telefono: ", bg="lightgreen")
    lbTelefono.place(x=20, y=300)
    telefono_ = Entry(ClientesWindow, width=25)
    telefono_.place(x=90,y=300)

    lbDireccion = Label(ClientesWindow, text="Direccion: ", bg="lightgreen")
    lbDireccion.place(x=20, y=335)
    direccion_ = Entry(ClientesWindow, width=45)
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