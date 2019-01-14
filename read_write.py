with open("Backend/python/notes/data/test.txt", "w") as testfile:
  testfile.write("Hello, C28.  hope you're having a great day")

with open("Backend/python/notes/data/test.txt", "a") as testfile:
    testfile.write("Here is more text")

# =================================

nickset = {"The Mooch", "Knuckles", "Burninator", "Kneecap", "Ole Red", "Bubba", "OG", "KitKat", "Spanky", "Monkeybutt", "L`il Devil", "Bird Person", "Fancy Slacks"}

nameset = {"Bob Smith", "Charise Anderson", "Jissie David", "Henry Goldberg", "Greg Korte", "Steve Brownlee", "Kimmy Bird", "Joe Shepherd", "Emily Lemmon", "Brenda Long", "Harold Brown", "Megan Ducharme", "Darth Vader"}




with open("Backend/python/notes/data/names.txt", "w") as names:
  for name in nameset:
    names.write(name + '\n')

with open("Backend/python/notes/data/nicks.txt", "w") as nicks:
  for nick in nickset:
    nicks.write(nick + '\n')

# Later, in some toher part of the app

with open("Backend/python/notes/data/names.txt", "r") as names:
  namelist = names.readlines()

with open("Backend/python/notes/data/nicks.txt", "r") as nicks:
  nicklist = nicks.readlines()



# Combining names and nicknames randomly

fullnames = [f"{name.strip().split(' ')[0]} \"{nicklist[i].strip()}\" {name.strip().split(' ')[1]}" for i, name in enumerate(namelist)]

print(fullnames)


