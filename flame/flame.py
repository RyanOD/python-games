import test_module

# remove shared characters
def merge_names(name1, name2):
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    return name1 + name2

def flame_names(combined_name):
    flame = ["friends", "lovers", "affectionate", "enemies", "married"]
    while len(flame) > 1:
        del flame[len(combined_name) % len(flame) - 1]
    return flame[0]

# get names from user
name1 = input("Please enter name of first person: ").lower()
name2 = input("Please enter name of second person: ").lower()

combined_name = merge_names(name1, name2)

print(f"{name1.capitalize()} and {name2.capitalize()} will be {flame_names(combined_name)}")