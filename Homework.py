import turtle

turtle.Screen().bgcolor("Purple")
sc = turtle.Screen()
sc.setup(400, 300)
turtle.title("Equilateral Triangle")

board = turtle.Turtle()

for i in range(3):
  board.forward(100)  
  board.left(120)     