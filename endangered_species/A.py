class Habitat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Species:
    def __init__(self, name, iucn_status, habitat, diet, unique_characteristics, id):
        self.name = name
        self.iucn_status = iucn_status
        self.habitat = Habitat(habitat)
        self.diet = diet
        self.unique_characteristics = unique_characteristics
        self.id = id

    def __str__(self):
        return f"{self.name} ({self.iucn_status})"

    def validate(self):
        # Check if name is not empty
        if not self.name:
            raise ValueError("Name cannot be empty")
        # Check if IUCN status is valid
        if self.iucn_status not in ["Extinct", "Critically Endangered", "Endangered", "Vulnerable", "Least Concern"]:
            raise ValueError("Invalid IUCN status")
        # Check if habitat is not empty
        if not self.habitat.name:
            raise ValueError("Habitat cannot be empty")
        # Check if diet is not empty
        if not self.diet:
            raise ValueError("Diet cannot be empty")
        # Check if unique characteristics is not empty
        if not self.unique_characteristics:
            raise ValueError("Unique characteristics cannot be empty")
        # Check if ID is unique
        if self.id in [species.id for species in species_list]:
            raise ValueError("ID must be unique")

species_list = []

def add_species(name, iucn_status, habitat_name, diet, unique_characteristics):
    habitat = Habitat(habitat_name)
    new_species = Species(name, iucn_status, habitat, diet, unique_characteristics, len(species_list) + 1)
    new_species.validate()
    species_list.append(new_species)

def edit_species(id, name, iucn_status, habitat_name, diet, unique_characteristics):
    species = get_species(id)
    if species:
        species.name = name
        species.iucn_status = iucn_status
        species.habitat.name = habitat_name
        species.diet = diet
        species.unique_characteristics = unique_characteristics
    else:
        raise ValueError("Invalid ID")

def get_species(id):
    return next((species for species in species_list if species.id == id), None)

def delete_species(id):
    species = get_species(id)
    if species:
        species_list.remove(species)
    else:
        raise ValueError("Invalid ID")

def view_species(id):
    species = get_species(id)
    if species:
        print(species)
    else:
        raise ValueError("Invalid ID")

def main():
    # Add some sample species
    add_species("Lion", "Vulnerable", "Savannah", "Carnivore", "Mane")
    add_species("Tiger", "Endangered", "Forest", "Carnivore", "Stripes")
    add_species("Elephant", "Least Concern", "Savannah", "Herbivore", "Tusks")

    # Edit a species
    edit_species(2, "Tiger", "Critically Endangered", "Forest", "Carnivore", "Stripes")

    # View a species
    view_species(1)

    # Delete a species
    delete_species(3)

if __name__ == "__main__":
    main()