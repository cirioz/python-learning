class Guitar:
    def __init__(self, n_strings=6):
        self.n_strings = n_strings
        self.play()
        self.__cost = 50

    #new method
    def play(self):
        print("pam pam pam")\

class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings=8)
        self.colour = ("#000000","#FFFFFF")
        
    def playLouder(self):
        print("pam pam pam".upper())
    def __secret(self):
        print("This guitar actually cost me $", self._Guitar__cost, "only!" )

class BassGuitar(Guitar):
    pass

my_guitar = ElectricGuitar()
my_guitar._ElectricGuitar__secret()

# print(BassGuitar(4).n_strings)
print(my_guitar.n_strings)




