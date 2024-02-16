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
        super().__init__("thumping")

class Piano(Instrument):
    def __init__(self):
        super().__init__("melodic")

class Band:
    def __init__(self, name, members, music_style):
        self.name = name
        self.members = members
        self.music_style = music_style

    def perform(self):
        sounds = []
        for member in self.members:
            sounds.append(member.play())
        return "".join(sounds)

# Create band members
guitarist = Guitar()
drummer = Drums()
pianist = Piano()

# Create a band
band_name = "The Melodic Mayhem"
band_members = [guitarist, drummer, pianist]
music_style = "Rock"

my_band = Band(band_name, band_members, music_style)

# Simulate a performance
performance = my_band.perform()
print(performance)