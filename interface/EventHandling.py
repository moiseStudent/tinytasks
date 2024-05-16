from abc import ABC
import tkinter as tk
import customtkinter
import frame

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
        
    def __create_task(self):
        """
        #! Pedir el titulo de la tarea, el titulo tiene que tener un numero maximo de caracteres
        #? Pedir la descripcion de la tarea, crear una ventana para el registro de estos datos
        #* Pedir la fecha limite para la tarea
        """
        pass

    def ___entry_data_layout(self):
        pass
    
    def check_entry_data(self):
        
        root = customtkinter.CTk()
        root.title("Esto seria una entrada de datos antes de poner el layout")
        root.geometry("400x400")
        
        textbox = customtkinter.CTkTextbox(root)

        textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
        text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
        textbox.delete("0.0", "end")  # delete all text
        textbox.configure(state="disabled")  # configure textbox to be read-only
        
        self.textbox = customtkinter.CTkTextbox(master=root, width=400, corner_radius=0)
        self.textbox.pack()
        self.textbox.insert("0.0", "Some example text!\n" * 50)       
        
    
        label = customtkinter.CTkLabel(root, text="Ingrese el nombre de la tarea")
        label.pack()
        
        entry_data = customtkinter.CTkEntry(root, width=300, height=300, placeholder_text="Ingrese los datos")
        entry_data.pack()
        
        btn = customtkinter.CTkButton(root, text="Agregar tarea", command = lambda: print(textbox.get("0.0", "end")))
        btn.pack()
        
        
        
        

        

    

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