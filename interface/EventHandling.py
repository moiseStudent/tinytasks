from abc import ABC
import json
import tkinter as tk
import customtkinter
from . import frame
from time import sleep

class ScrollBarFrame:
    
    def __init__(self, windows):
        self.windows = windows
        
        ### Barra de scroll
        self.my_frame = frame.ScrollableFrame(
            master=self.windows,
            width=500,
            height=200,
            corner_radius=0,
            fg_color="#333333"
            )
        
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        self.my_frame.new_task(place=[1,0], text="Titulo de la tarea")
    
    def add_task_layout(self, place):
        self.my_frame.new_task(place=place, text="Titulo de la tarea")

### Manage event
class ButtonEvent(ABC):
    
    def __init__(self):
        pass

### Add taks to the list
class AddTaskButtonEvent():
    
    def __init__(self):
        
        self.tasks = [] ### List taks saved in a file 
        self.data = {}  ### Object with the tasks' data
        
    def add_task(self, funcion_prueba = None):
        
        ### Entry data user for task ###
        self.__entry_data_layout()
        self.funcion = funcion_prueba
        
    def __save(self):
        with open("data/task/assets.json","w") as assets:
            json.dump(self.tasks,assets)     
    
        
    def __entry_data_layout(self):
        
        self.root = customtkinter.CTk()
        self.root.title("Agregar nueva tarea")
        self.root.geometry("420x420")
        
        self.textbox = customtkinter.CTkTextbox(master=self.root, width=400, corner_radius=0)
        self.textbox.grid(row=4, column=0, sticky="nsew")
        
        
        label = customtkinter.CTkLabel(
            self.root,
            text = "Ingrese el nombre de la tarea",
            height = 20
            )
        
        label.grid(row=0, column=0, padx = 10, pady = 10)
        
        self.entry_data = customtkinter.CTkEntry(
            
            self.root,
            width = 300,
            height=30,
            placeholder_text="Ingrese el nombre de la tarea"
            )
        
        self.entry_data.grid(row=1, column=0)
        
        button = customtkinter.CTkButton(
            self.root,
            text = "Agregar tarea",
            
            command = lambda: [
                
                self.get_entry_values,
                self.__create_task_layout,
                print("Se ha creado la tarea de forma exitosa."),
                self.close_windows()
                ]
        )
        button.grid(row=2, column=0)
    
    
    def __create_task_layout(self):
        
        ### Get place of file
        with open("data/task/assets.json", "r") as asserts:
            self.place = json.load(asserts)
            self.place = self.place[0] # In this part of data is the place of layout
            self.place = self.place['place']
        print(self.place)
        
        self.funcion(place=[2,0], text="Esta esta hecha desde otro sitio")
        ### Instance of frame ###
        self.frame = frame.Frame(
            self,place= [self.place['row'], self.place['column']],
            text = "Titulo de la tarea",
            width=400,
            fg_color='#2b2b2b'
            )
        
       # self.frame.grid(row=3, column=0, padx=20, pady=15, sticky='nsew')
        
       # self.frame(place=[2,0], text="Titulo de la tarea")
        
    def get_entry_values(self):
        
        ### Get data of input layout ###
        self.title_task = self.entry_data.get()
        self.details_task = self.textbox.get("0.0", "end")
        
        ### Data Dictionary ###
        self.data = {
            
            "place": {'row':2,'column':0},
            "title": self.title_task,
            "details": self.details_task,
            "date": "Sin fecha por los momentos" 
            
            }
        
        ### Add task at file ###
        self.tasks.append(self.data)
        self.__save()
       # self.__create_task_layout()
    
    
    def close_windows(self):
        ### Decir al usuario que se cerrara la ventana
        sleep(.5)
        self.root.destroy()

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