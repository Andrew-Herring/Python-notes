from car import Car
from color_picker import Color_picker

bumblebee = Car(34, 3, "cloth")
bumblebee.transformerize("dude", 5)
print("name?", bumblebee.v_type)

bumblebee_colors = Color_picker("yellow", interior="black", pinstripe="turquoise")
print(bumblebee_colors.get_colors())

bumblebee.add_colorscheme(bumblebee_colors.get_colors())

print(bumblebee.colorscheme)
