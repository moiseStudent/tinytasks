from abc import ABC
import json
import tkinter as tk
import customtkinter
from . import frame

### Manage event

class ButtonEvent(ABC):
    
    def __init__(self):
        pass


"""
Esta clase tiene que encargarse de hacer la tarea a nivel de datos y de recibir correcto los
datos, ademas de crear el layout de la ventana junto con el layout de ingreso de datos.
"""
### Add taks to the list
class AddTaskButtonEvent(ButtonEvent):
    
    def __init__(self):
        super().__init__()
        
        ### List taks saved in a file ###
        self.tasks = []
        
        ### Object with the tasks' data ###
        self.data = {}
        
    #! Esta funcion no la debe hacer esta parte del prgorama
    def __load(self):
        with open("../data/task/assets.json","r") as assets:

            try:                             
                self.tasks = json.load(assets)
                
            except (json.decoder.JSONDecodeError):
                self.__save()

    
    def __save(self):
        with open("data/task/assets.json","w") as assets:
            json.dump(self.tasks,assets)
    
    def add_task(self, title="Esto es un titulo", content="", date="Undefine"):
        self.__entry_data_layout()
        
        self.title = title
        self.content = content
        self.date = date
        
        ### Data Dictionary ###
        self.data = {
            
            "title": self.title,
            "details": self.content,
            "data": self.date
            
            } 
        
        self.__save()   

    def __entry_data_layout(self):
        
        root = customtkinter.CTk()
        root.title("Agregar nueva tarea")
        root.geometry("420x420")
        
        #! Traducir al ingles
        """
        Configuramos las filas y columnas de la ventana raíz (root) usando grid_rowconfigure()
        y grid_columnconfigure(). Establecemos weight=1 para indicar que las filas y columnas
        deben expandirse y centrar los elementos.
        """
        """
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)"""
        
        label = customtkinter.CTkLabel(
            root,
            text = "Ingrese el nombre de la tarea",
            height = 20
            )
        
        label.grid(row=0, column=0, padx = 10, pady = 10)
        
        self.entry_data = customtkinter.CTkEntry(
            
            root,
            width = 300,
            height=30,
            placeholder_text="Ingrese el nombre de la tarea"
            )
        
        self.entry_data.grid(row=1, column=0)
        
        button = customtkinter.CTkButton(
            root,
            text = "Revisar datos",
            command = self.get_entry_values
        )
        button.grid(row=2, column=0)
    
    def get_entry_values(self):
        value = self.entry_data.get()
        print(f"Esto son los datos que hay actualmente en el entry: {value}")
    
    def check_entry_data(self):
        pass
        
        
        
        

        

    

### Delete task in the list
class DeleteTaskButtonEvent(ButtonEvent):
    def __init__(self):
        super().__init__()

### Update the windows 
class UpdateWindowsButtonEvent(ButtonEvent):
    def __init__(self):
        super().__init__()

class ShowInfoTaskButtonEvent():
    def __init__(self):
        pass

    def show_info(self):
        root = customtkinter.CTk()
        root.title("Esto seria ver detalles")
        root.geometry("400x400")
    
### List of activities
class CheckListButtonEvent():
    def __init__(self):
        pass

### Instances
AddTaskButtonEvent = AddTaskButtonEvent()

### Delete task
DeleteTaskButtonEvent = DeleteTaskButtonEvent()

### Update Windows
UpdateWindowsButtonEvent =UpdateWindowsButtonEvent()

### SHow info in the button task
ShowInfoTakButtonEvent = ShowInfoTaskButtonEvent()

### Checklist options
CheckListButtonEvent = CheckListButtonEvent()