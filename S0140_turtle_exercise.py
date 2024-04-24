"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def visible():  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    print("x", -480 < turtle.position()[0] < 480)
    xinside = -480 < turtle.position()[0] < 480
    print("y", -480 < turtle.position()[1] < 480)
    yinside = -480 < turtle.position()[1] < 480
    return xinside and yinside


def square(lenght):
    turtle.speed(10)
    turtle.pencolor("blue")
    for i in range(4):
        turtle.forward(lenght)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()


def many_squares(amount, size, distance):
    for i in range(amount):
        turtle.forward(distance)
        turtle.pendown()
        square(size)
        size = size + size


def squiggle(s_length):
    turtle.pencolor("red")
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(150, 100)
    turtle.pendown()
    repetitions = int(s_length / 10)
    for i in range(repetitions):
        turtle.forward(s_length)
        turtle.right(90)
        turtle.forward(s_length)
        turtle.right(90)
        turtle.forward(s_length - 5)
        turtle.right(90)
        turtle.forward(s_length - 5)
        turtle.right(90)
        s_length = s_length - 10
    turtle.penup()


def star(points):
    if points > 6:
        angle = 360 / points * 4
    else:
        angle = 360 / points * 2
    for i in range(points):
        turtle.forward(150)
        turtle.right(angle)


def stars(first, second, third):
    turtle.pencolor("green")
    turtle.pensize(2)
    turtle.setheading(0)
    turtle.goto(-280, -200)
    turtle.pendown()
    star(first)
    turtle.penup()
    turtle.goto(-75, -236)
    turtle.pendown()
    star(second)
    turtle.penup()
    turtle.goto(125, -175)
    turtle.pendown()
    star(third)
    turtle.penup()


def thumbup():
    turtle.goto(-400, 0)
    turtle.setheading(0)
    turtle.pencolor("black")
    turtle.pendown()
    turtle.forward(100)
    for i in range(4):
        turtle.penup()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()
        turtle.forward(15)
        turtle.right(180)
        turtle.forward(15)
    turtle.penup()
    turtle.goto(-300, 0)
    for i in range(4):
        turtle.pendown()
        turtle.circle(10, 180)
        turtle.left(180)
    turtle.goto(-340, 80)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(30)
    turtle.circle(12, 130)
    turtle.setheading(-90)
    turtle.forward(39)
    turtle.setheading(-120)
    turtle.forward(30)
    turtle.setheading(180)
    turtle.goto(-400, 54)
    turtle.left(90)
    turtle.forward(54)
    turtle.done()


"""
def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.penup()
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


demo()
"""

length = 20

print(visible())
square(length)

many_squares(3, length + length, 10)

squiggle(100)

stars(5, 7, 11)

thumbup()
