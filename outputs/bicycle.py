from colour import Color
from chalk import *
from colour import Color
from chalk import *

black = Color("#000000")
blue = Color("#005FDB")

# Bicycle sizes
WHEEL_RADIUS = 1
FRAME_SIZE = 1.5 
SEAT_SIZE = 0.2
HANDLE_SIZE = 0.3

# Drawing the wheels of the bicycle
wheel = circle(radius=WHEEL_RADIUS).line_width(0.1) 

# Drawing the frame of the bicycle
frame1 = rectangle(width=2 * FRAME_SIZE, height=1).fill_color(blue).rotate(45)
frame2 = rectangle(width=2 * FRAME_SIZE, height=1).fill_color(blue).rotate(-45)
bikeFrame = vcat([hcat([frame1, frame2], sep= FRAME_SIZE), hcat([frame2, frame1], sep=FRAME_SIZE)])

# Drawing the seat of the bicycle
seat = square(side=SEAT_SIZE).fill_color(black)

# Drawing the handle of the bicycle
handle = square(side=HANDLE_SIZE).fill_color(blue)

# Putting the bicycle parts together
bicycle = vcat([
    hcat([wheel, bikeFrame, wheel], sep=WHEEL_RADIUS).center_xy(),
    vcat([seat, handle], sep=FRAME_SIZE).center_xy()
], sep=WHEEL_RADIUS)

bicycle.render("bicycle.png", 1200)

