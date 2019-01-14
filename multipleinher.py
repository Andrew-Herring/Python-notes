class Animal:
  def say_animal(self):
    return "I am an animal"


class Animal_Friend:
  def say_friend(self):
    return "My friend is Mr. Farmer"

class Cow(Animal, Animal_Friend):
  def say_cow_thing(self):
    print(f"{self.say_animal()} and {self.say_friend()}")
    # "I am an animal and my friend is Mr. Farmer"


# class Lion(Animal):  would not inherit from animal_friend

bossie = Cow()
bossie.say_cow_thing()  

# ========================

class Flying:
  def __init__(self):
    self.can_fly = True

  @property
  def wings(self):
    try:
        return self.__wing_count
    except AttributeError:
        return 2

  @wings.setter
  def wings(self, count):
    if isinstance(count, int):
      self.__wing_count = count
    else:
      raise TypeError("wing count must be a number")

  def fly(self):
    print("I can fly!")


class Swimming:
  def __init__(self):
    self.can_swim = True

  def swim(self):
    print("I can swim!")


class Running:
  def __init__(self, leg_length):
    self.can_run = True
    self.run_speed = 2.0
    self.leg_length = leg_length

  def run(self):
    if self.leg_length < 10 and self.run_speed <= 2.0:
      return "I'm waddling as fast as I can"
    elif self.leg_length < 20:
      return "I'm running now, but get closer and I'll fly instead"
    else:
      return "Catch me if you can"
      

class Bat(Flying):
  def __init__(self, species):
    self.has_feathers = False
    self.species = species




class Bird:
  def __init__(self, species, nest="tree"):
    self.has_feathers = True
    self.species = species
    self.nest = nest

  def lay_egg(self):
    if self.nest == "tree":
      return("Push! Breathe! Push!")
    else:
      return("Push! Breathe! Watch your step, please!")


class Penguin(Bird, Running, Swimming):

  def __init__(self, species, nest="ground", leg_length=5):
    self.color = "black and white"
    Bird.__init__(self, species, nest)
    Swimming.__init__(self)
    Running.__init__(self, leg_length)

  def __str__(self):
    return f"can_run: {self.can_run}, can_swim: {self.can_swim}, has_feathers: {self.has_feathers}"

emperor_penguin = Penguin("Emperor Penguin")
print("Our running, simming, feathery penguin", emperor_penguin)
