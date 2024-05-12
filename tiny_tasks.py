import os 
import json
from datetime import datetime
from colorama import Fore
from class_tasks import Tiny_task
from constant import *           

#?#######################################################################################################################

def current_date(): #* esta funcion sirve para saber la fecha actual en el formato "("%d/%m/%Y")"esto si yo o un contribuidor quiere agregar que expiren las tareas
    current_date = datetime.datetime.now() #*creacion de objeto extrayendo la fecha actual
    return current_date.strftime("%d/%m/%Y") #* formatear a el formato ("%d/%m/%Y")

def date_format(): #* esta funcion es para formatear las fechas
    try:
        date = input("introduce la fecha con el formato xx/xx/xxxx o dejalo en blanco si no quieres colocar fecha:  ")
        
        if date == "":#* esto es para que si no colocan nada aparezca fecha indefinida
            return None
        date_confirmed = datetime.datetime.strptime(date, "%d/%m/%Y")#* creacion de objeto de la clase datetime usando el string de la variable date y el formato de entrada ("%d/%m/%Y")
        #* dato curioso si en el formato se coloca la y minuscula en ves de ser xx/xx/xxxx seria xx/xx/xx
        return date_confirmed.strftime("%Y/%m/%d") #* retorna fecha formateada al reves para poder ordenarla bien en la funcion de tinytasks see_tasks()
    except ValueError:     #* cuando el formato de la fecha no es correcto entonces da valueError entonces vuelve a pedir la fecha
        print("fecha invalida o formato incorrecto intenta ingresarla con el formato xx/xx/xxxx(Si deseas salir presiona ctrl + c)")
        return date_format() #! si no se colocar return se acumulan funciones en bucle y si se coloca el formato correcto no se retorna 
#?########################################################################################################################

#? antes habia declarado un objeto de la clase 

#?########################################################################################################################

class Interface(Tiny_task): #* esta clase es la que ordena la interfaz 
    
    def __init__(self):  #*en el metodo init de la interface se pide que se elija una opcion donde se va a ejecutar cada una de las funciones de la interfaz y se va a repetir hasta que se interrumpa a travez del teclado o se presione 5 para salir
        
        Tiny_task.__init__(self)
        elect = self.show()
        if elect == "1":
            self.add()
        elif elect == "2":
            self.delete()
        elif elect == "3":
            self.change_order()
        elif elect == "4":
            self.delete()
        elif elect == "5":
            self.exit()
        elif elect.lower() == "r":
            self.factory_reset()
        else:
            input("Esa opcion no existe, recuerda que para seleccionar una opcion tienes que colocar lo que esta entre []\nPresiona enter para continuar:")
        self.__init__()
                                                                                                                                #?  que cuando se cree el objeto de una te pida que opcion quieres elegir y que tambien tenga un bucle
                                                                                                                                #? tambien seria bueno que un modulo pida la fecha para decir si la tarea ya expiro o no etc
    def show(self):#* aqui se ven las tareas y ordena la interfaz con las constantes de otro archivo
        os.system("cls" if os.name == "nt" else "clear") #* esto limpia la pantalla
        print(f"{INTERFACE_TITLE}\n\norden: {self.order_interface.capitalize()}\n{Tiny_task.see_tasks(self)}")
        return input(INTERFACE_OPTIONS)
    
    def add(self): #* aqui se piden las tareas y se formatea la fecha con date_format()
        self.titulo = input(f"\n{Fore.BLUE}Introduce el titulo de la tarea: {Fore.RESET}")
        self.contenido = input("Introduce detalles de la tarea: ")
        self.fecha = date_format()
        if self.fecha == None:
            return Tiny_task.add_task(self,self.titulo,self.contenido)
        Tiny_task.add_task(self,self.titulo,self.contenido,self.fecha)

    def delete(self):#* esta funcion borra una tarea 
        
        if self.tasks == []: #* si no hay tareas dara esto y volvera al metodo __init__()
            input("No hay tareas pora eliminar. ¯\_(ツ)_/¯ \nPresiona enter para continuar")
            return None
        os.system("cls" if os.name == "nt" else "clear") #* limpia pantalla
        print(INTERFACE_TITLE)
        print("\n"+self.see_tasks())
        tarea = input(DELETE_INTERFACE)                                                  #?arreglar error que cuando le das enter sin itroducir cualquier numero da error y tambien que cuando no hay tareas aun funciona
        print(tarea)
        try:
            Tiny_task.delete_task(self, tarea)
        except ValueError: #* esto esta por si se introduce una tarea invalida
            input("Esa tarea no es valida vuelve a intentarlo mas tarde. \nPresiona enter para continuar")
    
    def change_order(self): #* esta funcion esta para poder cambiar el orden de las tareas es decir que se ordene por titulo o por fecha (por ahora estan estas 2 mas adelante se podrian agregar mas como fecha de creacion etc)
        if self.order_interface == "titulo":
            self.order_interface = "fecha"
        else:
            self.order_interface= "titulo"
        self.save_order()
    
    def factory_reset(self): #* reseteo de fabrica en el caso de que se quiera borrar todo o de error por modificar los archivos assets1 y assets2
        reset = input(RESET_INTERFACE)
        if reset.lower() == "s":
            Tiny_task.factory_reset_tinytask()
        elif reset.lower() == "n":
            pass
        else:
            return self.factory_reset()

    def exit(self): #* salir. se explica solo
        exit()

#?####################################################################################################################################
#try: #* este codigo que esta en comentarios era una idea que era resetear de fabrica en el caso de un error general aunque luego pense que no era buena idea colocarlo
try:#* esto por si alguien quiere interrumpir con ctrl + c
    interface = Interface() 
except KeyboardInterrupt:
    print(f"\n\n{Fore.RED}Operacion interrumpida por el teclado\n")
#except:
#    input("parece que hay algo malo con el programa se va a reiniciar de fabrica \n presiona enter para continuar:")
#
#    Tiny_task.factory_reset_tinytask()



