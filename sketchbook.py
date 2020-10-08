# COMP1021 Lab 2 Python sketchbook

import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)

print("Welcome to the Python sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""
# Initialize fillcolour to "none" 
fillcolor = "none"

while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("q - Quit the program")
    print()

    option = input("Please input your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        # Ask user for angle
        angle = input("Please enter the angle by which you want to rotate the turtle: ")
        angle = int(angle)
        # Rotate turtle left
        turtle.left(angle)
        

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        # Ask user for height and width
        h = input("Please enter the height of the rectangle: ")
        h = int(h)
        w = input("Please enter the width of the rectangle: ")
        w = int(w)
        # Draw rectangle
        if fillcolor != "none":
            turtle.begin_fill
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        if fillcolor != "none":
            turtle.end_fill

    ##### Handle the circle option
    if option == "c":
        print()

        # Ask user for radius
        r = input("Please enter the radius of the circle: ")
        r = int(r)
        # Draw circle
        if fillcolor != "none":
            turtle.begin_fill
        turtle.circle(r)
        if fillcolor != "none":
            turtle.end_fill

    ##### Handle the pen colour option
    if option == "p":
        print()

        # Ask user for pen colour
        c = input("Please enter a colour name: ")
        # Change pen colour
        turtle.pencolor(c)

    ##### Handle the fill colour option
    if option == "f":
        print()

        # Ask user for colour
        fillcolor = input("Please enter a colour name (type \"none\" to clear the colour):")
        # Change fill colour
        if fillcolor != "none":
            turtle.fillcolor(f)

turtle.done()
