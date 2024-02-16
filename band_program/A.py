class Instrument:
    def __init__(self, sound, tuned=False):
        self.sound = sound
        self.tuned = tuned

    def play(self):
        if not self.tuned:
            print("Instrument out of tune!")
        return self.sound

    def tune(self):
        self.tuned = True

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

    def tune_instruments(self):
        for member in self.members:
            member.tune()

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

# Simulate a performance with out-of-tune instruments
print(my_band.perform())

# Tune the instruments
my_band.tune_instruments()

# Simulate a performance with in-tune instruments
print(my_band.perform())