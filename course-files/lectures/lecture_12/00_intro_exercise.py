import utilities

canvas = utilities.create_canvas_window()
user_data = input('Where should we draw your circle (input as x,y,radius)? ')  # 123,55,7
print(user_data)

## What do we do now?
#  1. We need to convert user_data into a form that can be used by the circle function
#  2. We need to invoke the utilities.make_circle function (that we made in HW1)