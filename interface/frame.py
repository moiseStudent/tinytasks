### Scroll frame
import customtkinter

class ScrollableFrame(customtkinter.CTkScrollableFrame):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Today")
        self.label.grid(row=0, column=0, padx=20, sticky='nsew')
        
    
    def new_task(self, place=[], text="Default"):
        
        self.frame = Frame(self,place=place,text = text, width=600)
        self.frame.grid(row=place[0], column=place[1], padx=20, pady=15)
        
    
class Frame(customtkinter.CTkFrame):
    
    def __init__(self, master, place, text, **kwargs):
        super().__init__(master,**kwargs)
        
        self.place = place
        self.text = text
        
        ### Label
        self.label = customtkinter.CTkLabel(self, text=self.text)
        self.label.grid(row=self.place[0],column=self.place[1], padx=10, pady=10)
        
        ### Button
        self.button = customtkinter.CTkButton(self, text=" Ver detalles")
        self.button.grid(row=self.place[0], column=self.place[1]+1, padx=10, pady=10)
        
        ### Check list
        self.check_list = customtkinter.CTkCheckBox(self, text="terminar")
        self.check_list.grid(row=self.place[0], column=self.place[1] + 2)
        

    

"""
frame = customtkinter.CTkFrame(master=root_tk, width=200, height=200)

my_frame = MyFrame(master=self)
my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

"""




    
        
        