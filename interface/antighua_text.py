        #! Esto es una prueba
        with open("data/task/place.txt", "w") as f:
            content = f.write("Esto es una prueba")
        
        with open("data/task/place.txt", "r") as f:
            print(f.read())
            
        
        with open("data/task/place.json", "w") as place:
            data = {"row":"Esto seria el valor de la row", "column":0}
            json.dump(data, place)
        
        with open("data/task/place.json", "r") as place:
            data = json.load(place)
            print(data["row"])
            
            
            
    #! Esta funcion no la debe hacer esta parte del prgorama
    def __load(self):
        with open("../data/task/assets.json","r") as assets:

            try:                             
                self.tasks = json.load(assets)
                
            except (json.decoder.JSONDecodeError):
                self.__save()