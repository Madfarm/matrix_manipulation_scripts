class Instrument:
    def __init__(self, name):
        self.name = name
                 
    def make_sound(self):
        print(f'{self.name} is making a sound.')

    def tune(self):
        print(f'{self.name} is being tuned.')
                  
      
class Guitar(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def strum(self):
        print(f'{self.name} is being strummed.')
                    
      
class Piano(Instrument):
    def __init__(self, name):
        super().__init__(name)
                              
    def play_chord(self):
        print(f'{self.name} is playing a beautiful chord.')

guitar = Guitar("guityar")
guitar.make_sound()
guitar.tune()
guitar.strum()

piano = Piano('Piano')
piano.make_sound()
piano.tune()
piano.play_chord()