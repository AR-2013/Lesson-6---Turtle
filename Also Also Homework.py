import turtle

turtle.Screen().bgcolor("Purple")
sc = turtle.Screen()
sc.setup(400, 500)
turtle.title("Hexagon")

board = turtle.Turtle()

for i in range(6):
   board.forward(100)  
   board.left(60)      