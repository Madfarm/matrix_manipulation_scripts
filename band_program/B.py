import random

class Instrument:
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        return self.sound

class Guitar(Instrument):
    def __init__(self):
        super().__init__("twangy")

class Drums(Instrument):
    def __init__(self):
        super().__init__("boomy")

class Piano(Instrument):
    def __init__(self):
        super().__init__("tinkly")

class Bass(Instrument):
    def __init__(self):
        super().__init__("thumpy")

class Vocals(Instrument):
    def __init__(self):
        super().__init__("singy")

class Band:
    def __init__(self, name, members, music_type):
        self.name = name
        self.members = members
        self.music_type = music_type

    def perform(self):
        sounds = []
        for member in self.members:
            sounds.append(member.play())
        return " ".join(sounds)

# Create band members
guitarist = Guitar()
drummer = Drums()
pianist = Piano()
bassist = Bass()
vocalist = Vocals()

# Create a band
band_name = "The Melodic Mayhem"
band_members = [guitarist, drummer, pianist, bassist, vocalist]
music_type = "Rock"

my_band = Band(band_name, band_members, music_type)

# Simulate a performance
print(my_band.perform())