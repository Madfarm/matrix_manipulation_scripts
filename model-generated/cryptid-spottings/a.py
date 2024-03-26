class Cryptid:
    def __init__(self, name, location, description, sightings=0):
        self.name = name
        self.location = location
        self.description = description
        self.sightings = sightings

    def increase_sightings(self):
        self.sightings += 1

    def track_sightings(self):
        return {self.name: self.sightings}

    def find_correlation(self, cryptids):
        locations = {}
        for cryptid in cryptids:
            if cryptid.location in locations:
                locations[cryptid.location] += 1
            else:
                locations[cryptid.location] = 1
        return locations


# Example usage
cryptid1 = Cryptid("Bigfoot", "North America", "Large ape-like creature covered in fur")
cryptid1.increase_sightings()
cryptid2 = Cryptid("Mothman", "West Virginia", "Tall, winged creature with glowing eyes")
cryptid2.increase_sightings()
cryptid2.increase_sightings()

print(cryptid1.track_sightings())
print(cryptid2.track_sightings())

cryptids = [cryptid1, cryptid2]
print(cryptid1.find_correlation(cryptids))