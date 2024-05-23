import os
import json
from datetime import datetime
import tkinter as tk
import customtkinter
from interface import frame
from interface.EventHandling import AddTaskButtonEvent, ScrollBarFrame
import threading
import subprocess

### Theme default app
customtkinter.set_appearance_mode('dark')

### Main class 
class Application():
    def __init__(self, windows, name='Default', geometry='500x500'):
        self.place = [2,0] #! El dato sera obtenido de un archivo place .json con las posiciones de
        #! Todas las tareas
        
        self.windows = windows
        self.name = name
        self.geometry = geometry
        
        ### Settings windows ###
        self.windows.title(self.name)
        self.windows.geometry(self.geometry)
        self.windows.grid_columnconfigure((0, 1), weight=1)
        self.windows.grid_rowconfigure(0, weight=1)
        
        ### More options
        self.button = customtkinter.CTkButton(
            self.windows,
            text="Poner aqui mas opciones",
            fg_color='#770000',
            text_color="#FFF690"
            )
        
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="sw", columnspan=2)
        
        ### This button - Update the windows
        self.button = customtkinter.CTkButton(
            self.windows,
            text="Actualizar la ventana",
            fg_color='#770000',
            text_color="#FFF690"
            )
        
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="ns", columnspan=1) 

        ### Add new taks in "data/task/assert.json" inside the file is the data
        self.button = customtkinter.CTkButton(
            self.windows,
            text="Agregar una Nueva Tarea",
            fg_color='#770000',
            text_color="#FFF690",
            command = self.__create_new_task
            )
        
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="se", columnspan=1)
        
        self.frame = ScrollBarFrame(self.windows)
        

    def __create_new_task(self):
        
        self.thread_one = threading.Thread(target=AddTaskButtonEvent.add_task())
        self.thread_one.start()
        
        self.frame.add_task_layout(place = [self.place[0], self.place[1] ] )     
        self.place[0] += 1
        

### app 
root = customtkinter.CTk()
try:
    logo = tk.PhotoImage(file="interface/imagenes/logo.png")

    root.config(background='#222222')
    root.iconphoto(True, logo)

except:
    pass

app = Application(root, name="Tiny Task")
root.mainloop()
