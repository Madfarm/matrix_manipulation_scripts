class Instrument:
    def init(self, name):
        self.name = name
                      
    def make_sound(self):
        pass

    def tune(self):
        pass

class StringInstrument(Instrument):
    def init(self, name, num_strings):
        super().init(name)
        self.num_strings = num_strings
                      
    def make_sound(self):
        return f'The {self.name} is playing a beautiful melody.'

    def tune(self):
        return f'The {self.name} is being tuned.'

    def pluck_string(self, string_number):
        if string_number > self.num_strings:
            return f'The {self.name} only has {self.num_strings} strings.'
        else:
            return f'String {string_number} on the {self.name} has been plucked.'
        
class WindInstrument(Instrument):
    def init(self, name, num_holes):
        super().init(name)
        self.num_holes = num_holes
                      
    def make_sound(self):
        return f'The {self.name} is playing a loud sound.'

    def tune(self):
        return f'The {self.name} is being tuned.'

    def blow_into(self, hole_number):
        if hole_number > self.num_holes:
            return f'The {self.name} only has {self.num_holes} holes.'
        else:
            return f'Blowing into hole {hole_number} on the {self.name}.'
        

guitar = StringInstrument('Guitar', 6)
print(guitar.make_sound())
print(guitar.tune())
print(guitar.pluck_string(3))
print(guitar.pluck_string(7))

trumpet = WindInstrument('Trumpet', 3)
print(trumpet.make_sound())
print(trumpet.tune())
print(trumpet.blow_into(2))
print(trumpet.blow_into(4))