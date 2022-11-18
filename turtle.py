







#6번문제
import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

def draw_star(aturtle, colour, side_length, x, y):
 t.color(colour)
 t.begin_fill()
 t.penup()
 t.goto(x, y)
 t.pendown()
 for i in range(5):
  t.forward(side_length)
  t.right(144)
  t.forward(side_length)
 t.end_fill()

for i in range(20):
 color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])
 side_length = random.randint(10, 100)
 x = random.randint(-200, 200)
 y = random.randint(-200, 200)
 draw_star(t, color, side_length, x, y)
