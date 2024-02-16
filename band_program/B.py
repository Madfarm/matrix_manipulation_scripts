class Instrument:
    def __init__(self, sound, tuned=False):
        self.sound = sound
        self.tuned = tuned

    def play(self, song):
        if not self.tuned:
            print("Instrument out of tune!")
        else:
            # Each instrument makes a different sound based on the song
            if song == "Song 1":
                self.sound += " tweedle"
            elif song == "Song 2":
                self.sound += " twang"
            elif song == "Song 3":
                self.sound += " thump"
            else:
                self.sound += " oops"
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
    def __init__(self, name, members, music_type, songs):
        self.name = name
        self.members = members
        self.music_type = music_type
        self.songs = songs

    def perform(self, song):
        # Check if instruments are in tune before playing
        if not all(member.tuned for member in self.members):
            print("Some instruments are out of tune! Please tune them first.")
            return

        sounds = []
        for member in self.members:
            sounds.append(member.play(song))
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
songs = ["Song 1", "Song 2", "Song 3"]

my_band = Band(band_name, band_members, music_type, songs)

# Simulate a performance with out-of-tune instruments
print(my_band.perform("Song 1"))

# Tune the instruments
my_band.tune_instruments()

# Simulate a performance with in-tune instruments
print(my_band.perform("Song 2"))