import tkinter as tk
import customtkinter
import frame

### Theme default app
customtkinter.set_appearance_mode('dark')

### Main class 
class Application():
    def __init__(self, windows, name='Default', geometry='500x500'):
        
        self.windows = windows
        self.name = name
        self.geometry = geometry
        
        ### Settings windows
        self.windows.title(self.name)
        self.windows.geometry(self.geometry)
        self.windows.grid_columnconfigure((0, 1), weight=1)
        self.windows.grid_rowconfigure(0, weight=1)
        
        ### Botones
        self.button = customtkinter.CTkButton(self.windows, text="Poner aqui mas opciones",fg_color='#770000',  text_color="#FFF690")
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="sw", columnspan=2)
        
        self.button = customtkinter.CTkButton(self.windows, text="Actualizar la ventana",fg_color='#770000',  text_color="#FFF690")
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="ns", columnspan=1)    #sw    
     
        self.button = customtkinter.CTkButton(self.windows, text="Agregar una Nueva Tarea",fg_color='#770000',  text_color="#FFF690")
        self.button.grid(row=1, column=0, padx=5, pady=10, sticky="se", columnspan=1)
        
        
        ### Barra de scroll
        self.my_frame = frame.ScrollableFrame(master=self.windows, width=500, height=200, corner_radius=0, fg_color="#333333")
        self.my_frame.grid(row=0, column=0, sticky="nsew")
        
        
        self.my_frame.new_task(place=[1,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[2,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[3,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[4,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[5,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[6,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[7,0], text="Titulo de la tarea")
        self.my_frame.new_task(place=[8,0], text="Titulo de la tarea")
        




### app 
root = customtkinter.CTk()

logo = tk.PhotoImage(file="imagenes/logo.png")

root.config(background='#222222')
root.iconphoto(True, logo)


app = Application(root, name="Tiny Task")

root.mainloop()
