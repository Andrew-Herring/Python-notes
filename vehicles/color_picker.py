class Color_picker:

  def __init__(self, primary_color, **kwargs):
    self.primary_color = primary_color
    for key, value in kwargs.items():
      setattr(self, key + "_color", value)


  def get_colors(self):
    return {k: v for k, v in self.__dict__.items() if 'color' in k}
      