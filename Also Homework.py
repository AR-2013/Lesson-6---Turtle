import turtle

turtle.Screen().bgcolor("Purple")
sc = turtle.Screen()
sc.setup(400, 300)
turtle.title("Rectangle")

board = turtle.Turtle()

for i in range(2):
  board.forward(120)  
  board.left(90)
  board.forward(60)   
  board.left(90)