from activity4_external import *

aso = Dog("Bogart", "Shitzu")
pusa = Cat("Muning", "Pusang kalye")

pets = []
pets.append(aso)
pets.append(pusa)

kim = Owner("Kim", pets)

for i in kim.getAllPets():
    print(i.getType())
