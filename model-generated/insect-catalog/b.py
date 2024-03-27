class Insect:
    def __init__(self, scientific_name, common_name, region, diet, lifespan, insect_id):
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.region = region
        self.diet = diet
        self.lifespan = lifespan
        self.insect_id = insect_id

class InsectCatalog:
    def __init__(self):
        self.catalog = {}

    def add_insect(self, insect):
        self.catalog[insect.insect_id] = insect

    def remove_insect(self, insect_id):
        if insect_id in self.catalog:
            del self.catalog[insect_id]
        else:
            print("Insect not found in the catalog.")

    def update_insect(self, insect_id, new_insect):
        if insect_id in self.catalog:
            self.catalog[insect_id] = new_insect
        else:
            print("Insect not found in the catalog.")

    def display_catalog(self):
        for insect_id, insect in self.catalog.items():
            print(f"ID: {insect_id}, Scientific Name: {insect.scientific_name}, Common Name: {insect.common_name}, Region: {insect.region}, Diet: {insect.diet}, Lifespan: {insect.lifespan}")

    def display_insect(self, insect_id):
        if insect_id in self.catalog:
            insect = self.catalog[insect_id]
            print(f"ID: {insect_id}, Scientific Name: {insect.scientific_name}, Common Name: {insect.common_name}, Region: {insect.region}, Diet: {insect.diet}, Lifespan: {insect.lifespan}")
        else:
            print("Insect not found in the catalog.")

# Creating insects
insect1 = Insect("Diptera", "Fly", "North America", "Omnivore", "1-2 years", 1)
insect2 = Insect("Hymenoptera", "Bee", "Global", "Herbivore", "1-5 years", 2)

# Creating catalog and adding insects
catalog = InsectCatalog()
catalog.add_insect(insect1)
catalog.add_insect(insect2)

# Displaying the catalog
catalog.display_catalog()

# Displaying specific insect
catalog.display_insect(1)

# Updating insect
new_insect1 = Insect("Diptera", "Fly", "North America", "Fruit", "1-2 years", 1)
catalog.update_insect(1, new_insect1)

# Removing insect
catalog.remove_insect(2)

# Displaying the catalog again
catalog.display_catalog()