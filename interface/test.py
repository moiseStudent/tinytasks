import customtkinter

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
        
        self.label1 = customtkinter.CTkLabel(self)
        self.label1.grid(row=1, column=0, padx=20)
        
        self.label2 = customtkinter.CTkLabel(self)
        self.label2.grid(row=2, column=0, padx=20)
        
        self.label3 = customtkinter.CTkLabel(self)
        self.label3.grid(row=3, column=0, padx=20)
        
        self.label4 = customtkinter.CTkLabel(self)
        self.label4.grid(row=4, column=0, padx=20)
        
        self.label01 = customtkinter.CTkLabel(self)
        self.label01.grid(row=5, column=0, padx=20)
        
        self.label102 = customtkinter.CTkLabel(self)
        self.label102.grid(row=6, column=0, padx=20)
        
        self.label203 = customtkinter.CTkLabel(self)
        self.label203.grid(row=7, column=0, padx=20)
        
        self.label304 = customtkinter.CTkLabel(self)
        self.label304.grid(row=8, column=0, padx=20)
        
        self.label405 = customtkinter.CTkLabel(self)
        self.label405.grid(row=9, column=0, padx=20)
        
        self.boton = customtkinter.CTkButton(self, text = "Elemento de prueba")
        self.boton.grid(row=10, column=1)
        
        
        


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
        self.my_frame.grid(row=0, column=0, sticky="nsew")


app = App()

scrollable_frame = customtkinter.CTkScrollableFrame(app, width=200, height=200)
app.mainloop()