class Cryptid:
    def __init__(self, name, location, description, sightings=0):
        self.name = name
        self.location = location
        self.description = description
        self.sightings = sightings

    def increment_sightings(self):
        self.sightings += 1

    def __str__(self):
        return f'{self.name} - {self.location} - {self.description} - {self.sightings} sightings'

class CryptidDatabase:
    def __init__(self):
        self.database = []

    def add_cryptid(self, cryptid):
        self.database.append(cryptid)

    def search_by_name(self, name):
        return [cryptid for cryptid in self.database if cryptid.name == name]

    def search_by_location(self, location):
        return [cryptid for cryptid in self.database if cryptid.location == location]

    def track_sightings_over_time(self):
        # This method should be implemented to track sightings over time
        pass

    def find_correlations(self):
        # This method should be implemented to find correlations between geographical areas and specific types of cryptids
        pass

# Example usage
db = CryptidDatabase()
db.add_cryptid(Cryptid('Bigfoot', 'North America', 'Large, hairy creature'))
db.add_cryptid(Cryptid('Loch Ness Monster', 'Scotland', 'Long-necked, serpentine creature'))
db.add_cryptid(Cryptid('Mothman', 'West Virginia', 'Winged, humanoid creature'))

print(db.search_by_name('Bigfoot'))
print(db.search_by_location('Scotland'))

# Increment sightings
for cryptid in db.search_by_name('Bigfoot'):
    cryptid.increment_sightings()

print(db.search_by_name('Bigfoot'))