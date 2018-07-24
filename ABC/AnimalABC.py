import abc

class Animal(abc.ABC):
    def __init__(self, species):
        super().__init__()
        self.species = species
    
    def describe(self,):
    	print("I am a {}".format(self.species))

    @abc.abstractmethod
    def makeSound(self): pass

    @abc.abstractmethod
    def move(self): pass