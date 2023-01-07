animals=[]

pet={
    'kind':'Dog',
    'name':'Jacky',
    'owner':'Ibrahim',
    'weight': 25,
    'eats': 'Meat',
}
#Use append to add each dictionary to the list
animals.append(pet)
pet={
    'kind':'Cat',
    'name':'Yams',
    'owner':'JJ',
    'weight': 12,
    'eats': 'MnM',
}
animals.append(pet)
pets={
    'kind':'Snake',
    'name':'Diablo',
    'owner':'Khiz',
    'weight': 5,
    'eats': 'rats',
}
animals.append(pets)
pets={
    'kind':'Iguana',
    'name':'Alvaro',
    'owner':'Hash',
    'weight': 43,
    'eats': 'bugs',
}
animals.append(pet)

for pet in animals:
    print("\nHere is what i know about " + pet['name'].title()+".")
    for key, value in pet.items():
        print("\t"+ key + ": " + str(value))
