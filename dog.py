class Dog:
    dog_name="Tek"
    def __init__ (self,name,size):
            self.name=name
            self.size=size
    def bark(self):
        return f"My {self.size} dog has lovely eyes"

    def jump(self):
        return f"My dog {self.name} loves running" 
