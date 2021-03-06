'''
Documentation: http://effbot.org/tkinterbook/canvas.htm
Color Picker: https://coolors.co/
'''

def make_label(canvas):
    canvas.create_text(
        (210, 210), 
        text="Hello world!", 
        font=("Purisa", 32),
        anchor='nw'  # align to "northwest" corner
    )

def make_oval(canvas):
    canvas.create_oval([ (50, 150), (150, 250) ],
        fill='#FF4136',
        width=5
    )

def make_polygon(canvas):
    canvas.create_polygon(
        [
            (370, 150), 
            (630, 150), 
            (500, 350)
        ],  # list of x-y pairs
        width=2,
        fill='#BCD39C',
        smooth=True)  #make smooth false for angular polygon


def make_solid_line(canvas):
    canvas.create_line(
        [
            (10, 0), 
            (210, 100), 
            (420, 0), 
            (630, 100)
        ],  # list of x-y pairs
        width=3)

def make_dashed_line(canvas):
    canvas.create_line(
        [
            (10, 100), 
            (210, 0), 
            (420, 100), 
            (630, 10)
        ], 
        fill="#3D9970", 
        dash=(4, 4), 
        width=3)


def make_curvy_line(canvas):
    canvas.create_line(
        [
            (0,   100), 
            (50,  150), 
            (100, 100), 
            (150, 150), 
            (200, 100), 
            (250, 150), 
            (300, 100), 
            (350, 150), 
            (400, 100)
        ], 
        splinesteps=20,
        width=3, 
        smooth=True)


def make_rectangle(canvas):
    canvas.create_rectangle(
        [
            (500, 25), 
            (650, 75)
        ],
        fill="#3D9970")


def make_arc(canvas):
    canvas.create_arc(
        [
            (250, 50), 
            (450, 350)
        ],
        width=5,
        style='arc',
        outline='#0074D9'
    )

# a convenience function for layout and debugging...this will make more sense in a few weeks.
def make_grid(c, w, h):
    interval = 100

    # Delete old grid if it exists:
    c.delete('grid_line')
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag='grid_line')

    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(
                x - offset, 
                y - offset, 
                x + offset,  
                y + offset, 
                fill='black'
            )
            c.create_text(
                x + offset, 
                y + offset, 
                text="({0}, {1})".format(x, y),
                anchor="nw", 
                font=("Purisa", 8)
            )
