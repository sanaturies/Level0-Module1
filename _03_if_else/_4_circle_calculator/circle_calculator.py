# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 

import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    radius=simpledialog.askinteger('title','radius?')
    choice=simpledialog.askstring('title','area or circumference?')

    if choice =='area':
        area=math.pi*radius**2
        messagebox.showinfo('title',area)
    else:
        cir=2*radius*math.pi
        messagebox.showinfo('title',cir)
