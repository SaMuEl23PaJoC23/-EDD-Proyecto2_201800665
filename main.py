from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from io import open
from PIL import Image, ImageTk
from graphviz import Graph
from datetime import datetime
import os

from circularDoble import CircularDoble
from listaSimple import ListaSimple

cd = CircularDoble()
ls = ListaSimple()

listaLugarescbox = []
listaDPIcbox = []
listaPLACAcbox = []
datosVehiculos = []
listaIDviajescbox = []
#===================== Funciones Ventana Main ============================
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

            #Se agregan rutas a lista lugarse comboBox, para poder ser usadas en comboBox de viaje, para ajilizar proceso
            if(ruta[0] not in listaLugarescbox):
                listaLugarescbox.append(ruta[0])

            if(ruta[1] not in listaLugarescbox):
                listaLugarescbox.append(ruta[1])
        
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
    btnClientes.place(x=25, y=14)
    btnVehiculos.place(x=218, y=14)
    btnViajes.place(x=400, y=14)
    btnReportes.place(x=220, y=103)
    btnVerMapaClaro.place(x=20, y=103)
    btnCargaMapa.place_forget() #Permite ocultar boton

def verMapa():
    os.startfile("grafoRutasMapa.png")

#------------------------------------------------------------------------
#--------ventana Clientes------------------------------------------------
def AbrirVentanaClientes():
    mainWindow.withdraw() #Oculta la ventana principal
    ClientesWindow = Toplevel(mainWindow)
    ClientesWindow.title("- Clientes -")
    ClientesWindow.geometry("480x370")
    ClientesWindow.config(bg="green")
    ClientesWindow.grab_set() #bloquea la interaccion con la ventana anterior
    centrarVentana(ClientesWindow)
    ClientesWindow.resizable(False, False)#Hace que no sea Redimensionable

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

                #Se agrega cliente a lista Circular
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
        if(dpi_.get()!="" and nombres_.get() !="" and apellidos_.get() !="" and genero_.get() !="" and telefono_.get() !="" and direccion_.get() !=""):
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

#-------------------------------------------------------------------------
#--------ventana Vehiculos------------------------------------------------
def AbrirVentanaVehiculos():
    mainWindow.withdraw() #Oculta la ventana principal
    VehiculosWindow = Toplevel(mainWindow)
    VehiculosWindow.title("- Vehiculos -")
    VehiculosWindow.geometry("480x370")
    VehiculosWindow.config(bg="brown")
    VehiculosWindow.grab_set() #bloquea la interaccion con la ventana anterior
    centrarVentana(VehiculosWindow)
    VehiculosWindow.resizable(False, False)#Hace que no sea Redimensionable

    def on_close():
        VehiculosWindow.grab_release() #Libera el bloqueo de eventos
        VehiculosWindow.destroy()
        mainWindow.deiconify() #Muestra nuevamente la ventana principal
    
    VehiculosWindow.protocol("WM_DELETE_WINDOW", on_close)
#--------Funciones ventana Clientes------------------------------------------------
    def cargaArchivoVehiculos():
        rutaArchivoVehiculos = filedialog.askopenfilename(initialdir="C:\\Users\\samal\\Desktop\\estructuas proyecto PYTHON") 
        if(rutaArchivoVehiculos != ""):
            archivoVehiculos = open(rutaArchivoVehiculos,"r")
            textoVehiculos = archivoVehiculos.readlines()
            archivoVehiculos.close()

            datosCargaVehiculo=[]
            vehiculos=[]
            for linea in textoVehiculos: #Se separan y almacenan las propiedades de cada Vehiculo
                datosCargaVehiculo = linea.split(':')
                vehiculos.append(datosCargaVehiculo)

            global listaPLACAcbox
            global datosVehiculos
            for vehiculo in vehiculos: #se remueve ';' y '\n'
                vehiculo[3] = vehiculo[3].replace(';','')
                vehiculo[3] = vehiculo[3].replace('\n','')

                #Se agregan Vehiculos a Arbol B
                listaPLACAcbox.append(vehiculo[0])
                datosVehiculos.append(vehiculo)

            actualizarComboBoxPlaca()
            messagebox.showwarning("Advertencia", "! Vehiculos Cargados !")

    def BloqueoCamposVehiculos():
        placa_.config(state='disabled')
        marca_.config(state='disabled')
        modelo_.config(state='disabled')
        precio_.config(state='disabled')

    def DesbloqueoCamposVehiculos():
        placa_.config(state='normal')
        marca_.config(state='normal')
        modelo_.config(state='normal')
        precio_.config(state='normal')
    
    def limpiarCamposVehiculos():
        placa_.delete(0, END)
        marca_.delete(0, END)
        modelo_.delete(0, END)
        precio_.delete(0, END)

    def actualizarComboBoxPlaca():
        lbPlacacBox.place(x=250, y=15)
        combxPlacaVehiculos.place(x=300, y=15) #Muestra ComboBox
        combxPlacaVehiculos["values"] = listaPLACAcbox
        combxPlacaVehiculos.set('')

    def seleccionPlaca(event):
        global datosVehiculos
        placaSeleccion = combxPlacaVehiculos.get()
        DesbloqueoCamposVehiculos()
        limpiarCamposVehiculos()
        for vehiculo in datosVehiculos:
            if(placaSeleccion == vehiculo[0]):
                placa_.insert(0, vehiculo[0])
                marca_.insert(0, vehiculo[1])
                modelo_.insert(0, vehiculo[2])
                precio_.insert(0, vehiculo[3])
                break
        BloqueoCamposVehiculos()

#--------Cuerpo Ventana Vehiculos---------------------------------------------------
    btnCargaVehiculos = Button(VehiculosWindow, text="Carga Masiva", bg="black", fg="white", command=cargaArchivoVehiculos)
    btnCargaVehiculos.place(x=20, y=5)

    lbPlacacBox = Label(VehiculosWindow, text="PLACA: ", bg="yellow")
    combxPlacaVehiculos = ttk.Combobox(VehiculosWindow, values=listaPLACAcbox, state="readonly")
    combxPlacaVehiculos.bind("<<ComboboxSelected>>", seleccionPlaca)

    btnAgregarVehiculo = Button(VehiculosWindow, text="Agregar Nuevo", bg="cyan")
    btnAgregarVehiculo.place(x=30, y=55)
    btnAgregarVehiculo.config(state='disabled')

    btnEditarVehiculo = Button(VehiculosWindow, text="Editar", bg="cyan")
    btnEditarVehiculo.place(x=40, y=105)
    btnEditarVehiculo.config(state='disabled')
    
    btnEliminarVehiculo = Button(VehiculosWindow, text="Eliminar", bg="cyan")
    btnEliminarVehiculo.place(x=200, y=55)
    btnEliminarVehiculo.config(state='disabled')

    btnVerVehiculosEstruct = Button(VehiculosWindow, text="Mostrar Estructura", bg="cyan")
    btnVerVehiculosEstruct.place(x=170, y=105)
    btnVerVehiculosEstruct.config(state='disabled')

    if(listaPLACAcbox != []):
        lbPlacacBox.place(x=250, y=15)
        combxPlacaVehiculos.place(x=300, y=15)

    lbPlaca = Label(VehiculosWindow, text="Placa: ", bg="red")
    lbPlaca.place(x=48, y=155)
    placa_ = Entry(VehiculosWindow, width=25)
    placa_.place(x=95,y=155)
    
    lbMarca = Label(VehiculosWindow, text="Marca: ", bg="red")
    lbMarca.place(x=43, y=190)
    marca_ = Entry(VehiculosWindow, width=25)
    marca_.place(x=95,y=190)

    lbModelo = Label(VehiculosWindow, text="Modelo: ", bg="red")
    lbModelo.place(x=35, y=225)
    modelo_ = Entry(VehiculosWindow, width=25)
    modelo_.place(x=95,y=225)

    lbPrecio = Label(VehiculosWindow, text="Precio (Q/s): ", bg="red")
    lbPrecio.place(x=15, y=260)
    precio_ = Entry(VehiculosWindow)
    precio_.place(x=95,y=260)

    BloqueoCamposVehiculos()

#------------------------------------------------------------------------
#--------ventana Viajes--------------------------------------------------
def AbrirVentanaViajes():
    mainWindow.withdraw() #Oculta la ventana principal
    ViajesWindow = Toplevel(mainWindow)
    ViajesWindow.title("- Viajes -")
    ViajesWindow.geometry("480x370")
    ViajesWindow.config(bg="gray")
    ViajesWindow.grab_set() #bloquea la interaccion con la ventana anterior
    centrarVentana(ViajesWindow)
    ViajesWindow.resizable(False, False)#Hace que no sea Redimensionable

    def on_close():
        ViajesWindow.grab_release() #Libera el bloqueo de eventos
        ViajesWindow.destroy()
        mainWindow.deiconify() #Muestra nuevamente la ventana principal
    
    ViajesWindow.protocol("WM_DELETE_WINDOW", on_close)
#--------Funciones ventana Viajes------------------------------------------------
    def BloqueoCamposViajes():
        idViaje_.config(state='disabled')
        origen_.config(state='disabled')
        destino_.config(state='disabled')
        fecha_.config(state='disabled')
        hora_.config(state='disabled')

    def DesbloqueoCamposViajes():
        idViaje_.config(state='normal')
        origen_.config(state='normal')
        destino_.config(state='normal')
        fecha_.config(state='normal')
        hora_.config(state='normal')

    def limpiarCamposViajes():
        idViaje_.delete(0, END)
        origen_.delete(0, END)
        destino_.delete(0, END)
        fecha_.delete(0, END)
        hora_.delete(0, END)

    def actualizaComboBoxViajes():
        global listaIDviajescbox
        listaIDviajescbox = ls.idViajesComboBox()
        combxIDviajes ["values"] = listaIDviajescbox
        combxIDviajes.set('')
        #Dado que no se elimina y unicamente se agrega en lista -listaIDviajescbox-, no se valida si en algun momento lista -listaIDviajescbox- este vacia
        lbIDviajes.place(x=240, y=15)
        combxIDviajes.place(x=300, y=15) 
        btnVerListaViaje.config(state='normal')
        btnVerEstructViajes.config(state='normal')

    def agregarNuevoViaje():
        lbIDviajes.place_forget()
        combxIDviajes.place_forget()
        DesbloqueoCamposViajes()
        limpiarCamposViajes()
        btnVerListaViaje.config(state='disabled')
        messagebox.showwarning("Advertencia", "Ya puede ingresar datos!")

        Fecha_hora_Actual = datetime.now()
        fecha_.insert(0, Fecha_hora_Actual.strftime("%Y/%m/%d"))
        hora_.insert(0, Fecha_hora_Actual.strftime("%H:%M:%S"))
        btnGuardar_viaje.place(x=320, y=260) #Muesta boton Guardar

        combxOrigen["values"] = listaLugarescbox
        combxOrigen.set('')
        combxDestino["values"] = listaLugarescbox
        combxDestino.set('')

        origen_.place_forget()
        destino_.place_forget()
        combxOrigen.place(x=105,y=190)
        combxDestino.place(x=105,y=225)

    def guardarNuevoViaje():
        if(idViaje_.get() !="" and combxOrigen.get() !="" and combxDestino.get() !="" and fecha_.get() !="" and hora_.get() !=""):
            if(combxOrigen.get() != combxDestino.get()):
                if(not ls.existenteEnSimple(idViaje_.get())):
                    btnGuardar_viaje.place_forget()
                    ls.agregarEnSimple(idViaje_.get(), combxOrigen.get(), combxDestino.get(), fecha_.get(), hora_.get())
                    
                    actualizaComboBoxViajes()

                    limpiarCamposViajes()
                    BloqueoCamposViajes()
                    btnVerListaViaje.config(state='normal')

                    combxOrigen.place_forget()
                    combxDestino.place_forget()
                    origen_.place(x=105,y=190)
                    destino_.place(x=105,y=225)

                    messagebox.showinfo("Atencion", "Datos guardado")    
                    print("\n=====Nueva Iteracion=====")
                    ls.ImprimirSimple()
            
                else:
                    idViaje_.delete(0, END)
                    messagebox.showerror("Alerta","ID viaje Ya existente...")
            
            else:
                messagebox.showerror("Alerta","Origen y Destino No pueden Coincidir!")

        else:
            messagebox.showerror("Alerta","Campo(s) vacio(s)...")

    def seleccionIDviaje(event):
        combxOrigen.place_forget()
        combxDestino.place_forget()
        origen_.place(x=105,y=190)
        destino_.place(x=105,y=225)
        seleccion_IDviaje = combxIDviajes.get()
        DesbloqueoCamposViajes()
        limpiarCamposViajes()

        datosViaje = ls.getDatosViaje(seleccion_IDviaje)
        idViaje_.insert(0, datosViaje.getIDviaje())
        origen_.insert(0, datosViaje.getLugarOrigen())
        destino_.insert(0, datosViaje.getLugarDestino())
        fecha_.insert(0, datosViaje.getFecha())
        hora_.insert(0, datosViaje.getHora())
        BloqueoCamposViajes()

    def verViaje():
        if(combxIDviajes.get() != ""):
            ls.graficarViaje(combxIDviajes.get())
        else:
            messagebox.showerror("Alerta","Primero debe seleccionar ID VIAJE")
    
    def verViajes():
        ls.graficarViajes()

#--------Cuerpo Ventana Clientes---------------------------------------------------
    lbIDviajes = Label(ViajesWindow, text="ID VIAJE: ", bg="lightblue")
    combxIDviajes = ttk.Combobox(ViajesWindow, values=listaIDviajescbox, state="readonly")
    combxIDviajes.bind("<<ComboboxSelected>>", seleccionIDviaje)

    btnVerListaViaje = Button(ViajesWindow, text="Ver viaje", bg="green", command=verViaje)
    btnVerListaViaje.place(x=20, y=10)
    btnVerListaViaje.config(state='disabled')

    btnVerEstructViajes = Button(ViajesWindow, text="Ver Viajes", bg="lightgreen", command=verViajes)
    btnVerEstructViajes.place(x=100, y=10)
    btnVerEstructViajes.config(state='disabled')

    btnAgregarViaje = Button(ViajesWindow, text="Nuevo Viaje", bg="cyan", command=agregarNuevoViaje)
    btnAgregarViaje.place(x=50, y=80)

    btnGuardar_viaje = Button(ViajesWindow, text="Guardar", bg="red", command=guardarNuevoViaje)

    if(listaIDviajescbox != []):
        lbIDviajes.place(x=240, y=15)
        combxIDviajes.place(x=300, y=15)
        btnVerListaViaje.config(state='normal')
        btnVerEstructViajes.config(state='normal')

    lbIDviaje = Label(ViajesWindow, text="ID Viaje: ", bg="lightgreen")
    lbIDviaje.place(x=44,y=155)
    idViaje_ = Entry(ViajesWindow, width=25)
    idViaje_.place(x=105,y=155)
    
    lbOrigen = Label(ViajesWindow, text="Lugar Origen: ", bg="lightgreen")
    lbOrigen.place(x=15, y=190)
    combxOrigen = ttk.Combobox(ViajesWindow, values=listaLugarescbox, state="readonly")
    origen_ = Entry(ViajesWindow, width=25)
    origen_.place(x=105,y=190)

    lbDestino = Label(ViajesWindow, text="Lugar Destino: ", bg="lightgreen")
    lbDestino.place(x=10, y=225)
    combxDestino = ttk.Combobox(ViajesWindow, values=listaLugarescbox, state="readonly")
    destino_ = Entry(ViajesWindow, width=25)
    destino_.place(x=105,y=225)

    lbFecha = Label(ViajesWindow, text="Fecha: ", bg="lightgreen")
    lbFecha.place(x=52, y=260)
    fecha_ = Entry(ViajesWindow)
    fecha_.place(x=105,y=260)

    lbHora = Label(ViajesWindow, text="Hora: ", bg="lightgreen")
    lbHora.place(x=56, y=295)
    hora_ = Entry(ViajesWindow)
    hora_.place(x=105,y=295)

    BloqueoCamposViajes()

#===================================================================================
#========================== Ajustes ventana main ===================================
mainWindow = Tk()
mainWindow.title("LLEGA RAPIDITO")
mainWindow.geometry("500x600")
mainWindow.config(bg='orange')
centrarVentana(mainWindow)
mainWindow.resizable(False, False)#Hace que no sea Redimensionable
#===================================================================================
#======================= CUERPO - MAIN =============================================
btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=cargaArchivoMapa) #PARA FUNCIONAMIENTO NORMAL, REMOVER ESTA LINEA
#btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=AbrirVentanaClientes) #PARA PROBAR VENTANA CLIENTES
#btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=AbrirVentanaVehiculos)  #PARA PROBAR VENTANA VEHICULOS
#btnCargaMapa = Button(mainWindow, text="INICIAR", bg="red", command=AbrirVentanaViajes)  #PARA PROBAR VENTANA VIAJES
btnCargaMapa.place(x=223, y=40)

btnClientes = Button(mainWindow, text="Clientes", bg="darkgreen", fg="white", command=AbrirVentanaClientes)

btnVehiculos = Button(mainWindow, text="Vehiculos", bg="darkgreen", fg="white", command=AbrirVentanaVehiculos)

btnViajes = Button(mainWindow, text="Viajes", bg="darkgreen", fg="white", command=AbrirVentanaViajes)

btnVerMapaClaro = Button(mainWindow, text="VER MAPA", bg="black", fg="white", command=verMapa)

btnReportes = Button(mainWindow, text="Reportes", bg="black", fg="white")

imagenLogo = Image.open("llegaRa.png")
nuevoSizeLogo = imagenLogo.resize((470,430), Image.LANCZOS)
paraMapa = ImageTk.PhotoImage(nuevoSizeLogo)

lbMapa = Label(mainWindow, image=paraMapa)
lbMapa.place(x=10, y=150)
#-----------------------------------------------------------------------
mainWindow.mainloop()