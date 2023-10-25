from colour import Color
from chalk import *

papaya = Color("#ff9700")
blue = Color("#005FDB")
# Define some constants for the sizing
WHEEL_RADIUS = 1
FRAME_SIZE = 2
SEAT_SIZE = 0.5
HANDLEBAR_WIDTH = 1

# Create color objects
black = Color("#000000")
orange = Color("#ff9700")

# Create two wheels
wheel = circle(radius=WHEEL_RADIUS).line_color(black)
wheels = hcat([wheel, wheel], sep=2*WHEEL_RADIUS)

# Create the frame of the bicycle
frame = vrule(length=FRAME_SIZE).line_color(orange)
frames = hcat([frame, frame], sep=2*WHEEL_RADIUS)

# Create a seat
seat = triangle(width=SEAT_SIZE).fill_color(blue)

# Create the handlebars
handlebar = hrule(length=HANDLEBAR_WIDTH).line_color(blue)

# Put them all together 
bicycle = vcat([wheels, frames, seat, handlebar], sep=0.1).center_xy()

bicycle.render("bicycle.png", 1200)
