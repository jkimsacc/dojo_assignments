name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    if len(name) >= len(favorite_animal):
        zip_dict = zip(arr1, arr2)
    else:
        zip_dict = zip(arr2, arr1)
    for index in range(0, len(zip_dict)):
        new_dict[zip_dict[index][0]] = zip_dict[index][1]
    return new_dict

print make_dict(name, favorite_animal)
