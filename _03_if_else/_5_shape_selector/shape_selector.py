import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    t=turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shapes=simpledialog.askstring('title','shape?')
    # Draw the shape requested by the user using if-elif-else statements
    if shapes =='circle':
        t.circle(100)
    elif shapes == 'square':
        for i in range(4):
            t.forward(100)
            t.right(90)
    elif shapes == 'triangle':
        for i in range(3):
            t.forward(100)
            t.right(120)
    # Call the turtle .done() method
    turtle.done()
