from abc import ABC
import json
import tkinter as tk
import customtkinter
from . import frame

### Manage event
class ButtonEvent(ABC):
    
    def __init__(self):
        pass

### Add taks to the list
class AddTaskButtonEvent(ButtonEvent):
    
    def __init__(self):
        super().__init__()
        
        self.tasks = [] ### List taks saved in a file 
        self.data = {}  ### Object with the tasks' data
        
    def add_task(self):
        
        ### Entry data user for task ###
        self.__entry_data_layout()
        

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
            command = self.get_entry_values
        )
        button.grid(row=2, column=0)
    
    
    def __create_task_layout(self):
        
        ### extrac place of data
        with open("data/task/assets.json", "r") as d:
            self.t = json.load(d)
            self.t = self.t[0]
            self.t = self.t['place']
            self.t = self.t['row']
        print(self.t)
        """
        self.frame = frame.Frame(self,place= place,text = text, width=400, fg_color='#2b2b2b')
        self.frame.grid(row=place[0], column=place[1], padx=20, pady=15, sticky='nsew')
        """
    def get_entry_values(self):
        
        self.title_task = self.entry_data.get()
        self.details_task = self.textbox.get("0.0", "end")
        
        ### Data Dictionary ###
        self.data = {
            
            "place": {'row':'la row funciona','column':1},
            "title": self.title_task,
            "details": self.details_task,
            "date": "Sin fecha por los momentos" 
            
            }
        
        ### Add task at file ###
        self.tasks.append(self.data)
        self.__save()
        
        self.__create_task_layout()
        
        print(self.title_task, self.details_task)

    
    
    
    
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