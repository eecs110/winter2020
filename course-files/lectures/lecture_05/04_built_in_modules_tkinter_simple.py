from tkinter import Canvas, Tk
gui = Tk()
gui.title('Shapes')
canvas = Canvas(gui, width=500, height=300, background='white')
canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

canvas.create_rectangle([
        (200, 100),  # top_left
        (300, 200)  # bottom_right
    ],
    fill='teal'
)

########################## YOUR CODE ABOVE THIS LINE ############################## 
# makes sure the canvas keeps running:
canvas.mainloop()