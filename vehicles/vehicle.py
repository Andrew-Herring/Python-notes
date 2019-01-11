# Base class for creating vehicles of any kind
class Vehicle:

    def __init__(self, v_type="vehicle"):
      self.name = "Vehicle"
      self.v_type = v_type
      self.is_transformed = False

    def add_wheels(self, wheel_num):
      self.wheels = wheel_num

    def _add_rockets(self, rocket_num):
      self.rockets = rocket_num

    def transformerize(self, bot_name, rocket_num):
      self._add_rockets(rocket_num)
      self.wheels = 0
      self.is_transformed = True
      self.bot_name = bot_name

    def add_colorscheme(self, colors_obj):
      self.colorscheme = colors_obj

    def __str__(self):
      return f"This vehicle's name is {self.name}!"