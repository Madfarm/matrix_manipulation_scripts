class Insect:
    insect_list = []

    def __init__(self, scientific_name, common_name, region, diet, lifespan, insect_id):
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.region = region
        self.diet = diet
        self.lifespan = lifespan
        self.insect_id = insect_id
        Insect.insect_list.append(self)

    @classmethod
    def add_insect(cls, scientific_name, common_name, region, diet, lifespan, insect_id):
        insect = cls(scientific_name, common_name, region, diet, lifespan, insect_id)
        return insect

    @classmethod
    def remove_insect(cls, insect_id):
        for insect in cls.insect_list:
            if insect.insect_id == insect_id:
                cls.insect_list.remove(insect)
                return f"Insect with ID {insect_id} removed."
        return "Insect not found."

    @classmethod
    def update_insect(cls, insect_id, attribute, value):
        for insect in cls.insect_list:
            if insect.insect_id == insect_id:
                setattr(insect, attribute, value)
                return f"Insect with ID {insect_id} updated."
        return "Insect not found."

    @classmethod
    def display_insect(cls, insect_id=None):
        if insect_id:
            for insect in cls.insect_list:
                if insect.insect_id == insect_id:
                    return vars(insect)
            return "Insect not found."
        else:
            return [vars(insect) for insect in cls.insect_list]


# Adding insects
Insect.add_insect('Diptera', 'Flies', 'North America', 'Omnivorous', '2 days', '123')
Insect.add_insect('Lepidoptera', 'Butterflies', 'South America', 'Herbivorous', '2 weeks', '456')

# Displaying all insects
print(Insect.display_insect())

# Displaying a specific insect
print(Insect.display_insect('123'))

# Updating an insect
print(Insect.update_insect('123', 'diet', 'Carnivorous'))

# Removing an insect
print(Insect.remove_insect('456'))

# Displaying all insects after removal
print(Insect.display_insect())