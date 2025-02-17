class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("pet must be a Pet")
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)