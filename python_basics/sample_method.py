def make_sound(animal):
    if animal == "cat":
        return "meow"
    elif animal == "fox":
        return "timtirimtim"
    elif animal == "dog":
        return "bark"
    else:
        return "no animal"


sound = make_sound("fox")
print(sound)
