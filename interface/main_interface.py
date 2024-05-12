import tkinter as tk
import customtkinter


### Modo dark en la app
customtkinter.set_appearance_mode('dark')

class MyFrameScrollable(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

        self.label1 = customtkinter.CTkLabel(self)
        self.label1.grid(row=1, column=0, padx=20)
        
        self.label2 = customtkinter.CTkLabel(self)
        self.label2.grid(row=2, column=0, padx=20)


class MyFrame(customtkinter.CTkFrame):
    
    def __init__(self, master,text='Label', **kwargs):
        super().__init__(master, **kwargs)
        
        self.text = text
        ## Agregar widwet a los Frame
        self.label = customtkinter.CTkLabel(self, text = self.text)
        self.label.grid(row=1,column=1,padx=40, pady=20)
        
        self.boton = customtkinter.CTkButton(self, text = self.text)
        self.boton.grid(row=3, column=1)

class Application():
    
    def __init__(self, app, title="Default", geometry="300x300"):
        
        self.app = app
        
        ### General settings windows
        self.app.title(title)
        self.app.geometry(geometry)
        #self.app.grid_columnconfigure((0, 1), weight=1)
        #self.app.grid_rowconfigure(0, weight=1)
        
        # My frame
        
        self.my_frameScroll = MyFrameScrollable(master=self.app, width=500, height=500, corner_radius=0, fg_color="transparent")
        self.my_frameScroll.grid(row=0, column=0, sticky="nsew")
        
        self.my_frame = MyFrame(master=self.app, width=500, border_width=5)
        self.my_frame.grid(row=1, column=0, padx=40, pady=20) # sticky="nsew"
        
        self.newF = MyFrame(master=self.app, width=500, border_width=5)
        self.newF.grid(row=2, column=0, padx=40, pady=20) # sticky="nsew"
        
        self.my_frame1 = MyFrame(master=self.app, width=500, border_width=5)
        self.my_frame1.grid(row=1, column=0, padx=40, pady=20) # sticky="nsew"
        
        self.newF2 = MyFrame(master=self.app, width=500, border_width=5)
        self.newF2.grid(row=2, column=0, padx=40, pady=20) # sticky="nsew"
        
        
    
    def create_task(self):
        
        button = customtkinter.CTkButton(self.app, text="Prueba")
        button.grid(row=0, column=0)
        




### Windows instance
root = customtkinter.CTk()

app = Application(root, title = "Tiny Task", geometry="600x600")
app.create_task()



root.mainloop()