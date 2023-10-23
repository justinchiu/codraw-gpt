from colour import Color
from chalk import *

papaya = Color("#ff9700")
blue = Color("#005FDB")

d = circle(1).fill_color(papaya)

d.render("figures/intro-01.png", height=64)
