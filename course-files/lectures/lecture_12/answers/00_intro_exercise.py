import utilities

user_data = input('Where should we draw your circle (input as x,y,radius)? ')  # 200,200,50

## What do we do?
nums = user_data.split(',')
x = int(nums[0])
y = int(nums[1])
r = int(nums[2])

canvas = utilities.create_canvas_window()
utilities.make_circle(canvas, (x, y), r, color='teal')
canvas.mainloop()