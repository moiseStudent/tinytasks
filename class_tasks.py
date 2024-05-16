import os 
import json
from colorama import Fore
import datetime
#?######################################################################################################################################

#* el creador de este programa es: Luis Fajardo alias pinguinaje360 en github


#?######################################################################################################################################

#*comentarios del programa con la extension de vscode bettercomments

#? notas propias
#* notas para otro programador que lea el programa
#!notas que dejo para recordar algo que capaz pueda usar luego

#?#####################################################################################################################################

#!importe os para poder cambiar la ruta de trabajo y importe json para poder usar archivos json para guardan el estado del programa
#? cambiar ruta de trabajo a la misma del archivo para evitar crear archivos en lugares donde no se quiere

#? la idea seria crear un objeto que tenga como clase tiny task
#! chdir = change directory, getcwd = get current working directory, listdir = es para mostrar todas los archivos de nuestro directorio y devuelve una lista,
#! mkdir = make directory(se usa asi: os.mkdir("nombre del directorio" y da error si ya existe))

#?#######################################################################################################################################

class Tiny_task: #* esta clase gestiona todo internamente
    
    def factory_reset_tinytask(self): #* esta funcion borra dos los archivos de assets para que se reinicie de fabrica el programa
        os.remove("data/task/assets.json")
        os.remove("data/task/assets2.json") 

    def load(self):               #* esta funcion sirve para poder cargar todo el contenido del archivo assets1.json a la variable self.tasks
        with open("data/task/assets.json","r") as assets:
                try:                              #? este try y except estan puestos para que si en el hipotetico caso de que alguien borre el contenido del archivo JSON entonces no deje de funcionar el programa
                    self.tasks = json.load(assets)
                except (json.decoder.JSONDecodeError):
                    self.save()

    def save(self):               #* esta funcion sirve para guardar todo el contenido de la variable self.tasks dentro del archivo assets.json
        with open("data/task/assets.json","w") as assets:
            json.dump(self.tasks,assets)

    def load_order(self):         #*esta funcion hace lo mismo que la funcion load() solo carga el contenido del archivo assets2.json a order_interface
        with open("data/task/assets2.json","r") as assets:
                try:                              #* este try y except estan puestos para que si en el hipotetico caso de que alguien borre el contenido del archivo JSON entonces no deje de funcionar el programa
                    self.order_interface = json.load(assets)
                except json.decoder.JSONDecodeError:
                    self.save_order()

    def save_order(self):         #*este tambien hace lo mismo pero con la variable self.order_interface
        with open("data/task/assets2.json","w") as assets:
            json.dump(self.order_interface,assets)

    def __init__(self):           #* este metodo sirve para que la ruta de trabajo se cambie por la del archivo actual y tambien carga todo
                                #* con load() y load_order() y en el caso que no existan los archivos assets1 y assets2 se van a crear 
                                #*por esta razon funciona el reseteo de fabrica
        os.chdir(os.path.dirname(__file__))
        self.order_interface = "titulo"
        self.tasks = []
        try:
            self.load()
            self.load_order()
                        #? este try y except esta puesto para que cuando alguien ejecute el programa por primera vez no de ese error; que significa el archivo no fue encontrado y se ejecute el programa correctamente
        except FileNotFoundError :
            self.save()
            self.save_order()

    def see_tasks(self): #* esta funcion devuelve las tareas formateadas
        self.load()#*carga las tareas a la variable self.tasks
                                                                                                                            #? estas son variables de instancia y las que se declaran fuera de los metodos son variables de clase//// la diferencia es que las variables de instancia se tiene que crear un objeto antes usar la variable mientras que en la variable de clase se puede usar sin crear un objeto usando nombredeclase.variabledeclase
                                                                                                                            #? el try es para que en el caso de que no haya "" en el diccionario ps no se detenga el programa
        
        n = 1    #* en esta parte se ordenan las tareas segun la clave que haya en la variable self.order_interface, por ahora solo estan las opciones por fecha y titulo 
        self.tasks.sort( key = lambda x: x[self.order_interface])   
                                                           #! mañana tengo que convertir de alguna manera las fechas en objetos de la clase datetime para poder compararlas
        string=""    
                                                                                                              #! mi idea es hacer que se guarde con el formato 2024/12/31 para luego convertir esa fecha/string a un objeto y luego de nuevo formatearla al imprimirla
        for i in self.tasks: #* bucle para sacar todo el contenido de la lista self.tasks
            if i["fecha"]!= "indefinido":
                fecha_object = datetime.datetime.strptime(i["fecha"],("%Y/%m/%d"))#* aca se crea un objeto de la clase datetime y se coloca el string de la fecha y el formato de entrada
                string += f"\n[{n}] Titulo: {i['titulo']}\n    Detalles: {i['detalles']}\n    Fecha: {fecha_object.strftime('%d/%m/%Y')}\n" #* y aca se imprime el titulo, los detalles y la fecha cambiando el formato por este "%d/%m/%Y"
                n+=1   #* enumerar por cada tarea 
            else: #* esto es por si la fecha es indefinida para que no de error al intentar crear el objeto datetime
                string += f"\n[{n}] Titulo: {i['titulo']}\n    Detalles: {i['detalles']}\n    Fecha: {i['fecha']}\n" 
                n+=1   #* enumerar por cada tarea 
        return string 


    def add_task(self,titulo,contenido = "",fecha = "indefinido"):  #* esta funcion es para agregar tarea y se recibe los valores: titulo contenido y fecha y si guardan en un diccionario dentro de una lista cada tarea
        self.title = titulo
        self.content = contenido
        self.date = fecha
        self.data = {"titulo": self.title,"detalles": self.content,"fecha": self.date} #* al guardar la fecha se guarda con el formato 2024/12/31
        self.tasks.append(self.data) 
        self.save()

    def delete_task(self,number): #* borrar tarea donde se borra el numero que ingreso el usuario restandole -1 para que coincida con el indice de la lista self.tasks que ya esta ordenada al ejecutarse see_tasks()
        try:
            del(self.tasks[int(number)-1])
            self.save()

        except IndexError:
            input("Esa tarea no existe.\nPresiona enter para continuar.") #* si la tarea no existe 
                                            # identificar las tareas con numeros
        
