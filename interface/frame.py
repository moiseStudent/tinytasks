### Scroll frame
import customtkinter
from .EventHandling import ShowInfoTaskButtonEvent, AddTaskButtonEvent

class ScrollableFrame(customtkinter.CTkScrollableFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Today", bg_color='#4c4c4c', text_color='#ffffff')
        self.label.grid(row=0, column=0, padx=20, sticky='nsew')
        
    #! Esta funcion desde el archivo EventHandling para tener mas extension en el codigo
    #! No pedir argumentos, debe ser entregados desde el layout que se crea en Event handling
    def new_task(self, place=[], text="Default"):
        
        AddTaskButtonEvent.add_task
        
        self.frame = Frame(self,place=place,text = text, width=400, fg_color='#2b2b2b')
        self.frame.grid(row=place[0], column=place[1], padx=20, pady=15, sticky='nsew')
        
    
class Frame(customtkinter.CTkFrame):
    
    def __init__(self, master, place, text, **kwargs):
        super().__init__(master,**kwargs)
        
        self.place = place
        self.text = text
        
        ### Label
        self.label = customtkinter.CTkLabel(self, text=self.text)
        self.label.grid(row=self.place[0],column=self.place[1], padx=10, pady=10,sticky='sw')
        
        ### Button
        self.button = customtkinter.CTkButton(
            self,
            text = " Ver detalles",
            fg_color = "#19238C",
            text_color = '#FCFEEE',
            command = ShowInfoTaskButtonEvent.show_info
            )
        self.button.grid(row=self.place[0], column=self.place[1]+1, padx=10, pady=10, sticky='ns')
        
        ### Check list
        self.check_list = customtkinter.CTkCheckBox(self, text="")
        self.check_list.grid(row=self.place[0], column=self.place[1] + 2, sticky='sen')

"""
Para hacer ventanas sin tener que escribir tantas lineas de codigo
"""
class GeneralFrame(customtkinter.CTkFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
    