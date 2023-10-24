from colour import Color
from chalk import *
from colour import Color
from chalk import *

# define colors
black = Color("#000000")
blue = Color("#005FDB")

# define sizes
WHEEL_RADIUS = 1
WHEEL_SPACE = 1
FRAME_SIZE = 1
HANDLE_WIDTH = 0.5
SEAT_HEIGHT = 1.5

# create wheels
outer_wheel = circle(radius=WHEEL_RADIUS).fill_color(black)
inner_wheel = circle(radius=0.3 * WHEEL_RADIUS).fill_color(blue)
wheel = concat([outer_wheel, inner_wheel])

# create two wheels
wheels = hcat([wheel, wheel], sep=WHEEL_SPACE).center_xy()

# create frame
upper_frame = hrule(length=FRAME_SIZE).line_color(blue)
lower_frame = hrule(length=FRAME_SIZE).line_color(blue)
frame = vcat([upper_frame, lower_frame], sep=0.1).center_xy()

# create handle
handle_stem = vrule(length=WHEEL_RADIUS).line_color(blue)
handle = hrule(length=HANDLE_WIDTH).line_color(blue).align_t()
handle = concat([handle, handle_stem])

# create seat
seat_stem = vrule(length=SEAT_HEIGHT).line_color(blue)
seat = hrule(length=HANDLE_WIDTH).line_color(blue).align_t()
seat = concat([seat, seat_stem])

# put everything together
bicycle = concat([wheels, frame.align_bl(), handle.align_br(), seat.align_bl()]).center_xy()

bicycle.render_svg("bicycle.svg", height=128)
