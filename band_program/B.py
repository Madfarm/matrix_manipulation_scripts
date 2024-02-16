class Instrument:
    def __init__(self, sound, tuned=False):
        self.sound = sound
        self.tuned = tuned

    def play(self, song):
        if not self.tuned:
            print("Instrument out of tune!")
        else:
            if song == "Song 1":
                return self.sound + " (Song 1 version)"
            elif song == "Song 2":
                return self.sound + " (Song 2 version)"
            else:
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
        sounds = []
        for member in self.members:
            sounds.append(member.play(song))
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
songs = ["Song 1", "Song 2", "Song 3"]

my_band = Band(band_name, band_members, music_type, songs)

# Simulate a performance of Song 1
print(my_band.perform("Song 1"))

# Simulate a performance of Song 2
print(my_band.perform("Song 2"))