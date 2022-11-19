#4번 문제
import turtle      #터틀 라이브러리를 가져옴
import random           #랜덤 라이브러리를 가져옴
t = turtle.Turtle()        #터틀 모듈에 터틀 함수를 t로 선언
t.shape("turtle")           #모양을 거북이로 설정

def draw_square(x, y, c):      #draw_square(x, y, c) 함수 선언
 t.up()                    #거북이가 이동할 때 선 생기지 않음
 t.goto(x, y)              #좌표 (x, y) 이동
 t.down()              #거북이 이동할 때 선 생김
 t.color("black",c)
 t.begin_fill()         #도형안에 색깔을 칠하기 위해 준비
 t.forward(100)          #100만큼 전진
 t.left(90)             #왼쪽으로 90도 회전
 t.forward(100)        #100만큼 전진
 t.left(90)             #왼쪽으로 90도 회전
 t.forward(100)          #100만큼 전진
 t.left(90)                   #왼쪽으로 90도 회전
 t.forward(100)              #100만큼 전진
 t.left(90)                #왼쪽으로 90도 회전
 t.end_fill()                  #도형 안에 색깔 칠하고 종료
for c in ["yellow", "red", "purple", "blue"]:
 x = random.randint(-100, 100)
 y = random.randint(-100, 100)
 draw_square(x, y, c)             # draw_square(x, y, c)함수 사용
 

#5번 문제
import turtle             #터틀 라이브러리를 가져옴
import random           #랜덤 라이브러리를 가져옴


t = turtle.Turtle()             #터틀 모듈에 터틀 함수를 t로 선언
s = turtle.Screen()          #그림 그려지는 화면 얻음


def draw_shape(t, c, length, sides, x, y):         #draw_shape(t, c, length, sides, x, y) 함수 선언
 t.up()                    #거북이가 이동할 때 선 생기지 않음
 t.goto(x, y)               #좌표 (x, y) 이동
 t.down()                 #거북이 이동할 때 선 생김
 t.fillcolor(c)
 angle = 360.0 / sides
 t.begin_fill()            #도형안에 색깔을 칠하기 위해 준비
 for dist in range(sides):
  t.forward(length)
  t.left(angle)
 t.end_fill()              #도형 안에 색깔 칠하고 종료

for i in range(10):               #10번 반복
 color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])       #컬러는 랜덤으로 사용됨
 side_length = random.randint(10, 100)
 sides = random.randint(3, 10)
 x = random.randint(-200, 200)
 y = random.randint(-200, 200)
 draw_shape(t, color, side_length, sides, x, y)            #draw_shape(t, c, length, sides, x, y)함수 사용


#6번문제
import turtle               #터틀 라이브러리를 가져옴
import random              #랜덤 라이브러리를 가져옴
t = turtle.Turtle()             #터틀 모듈에 터틀 함수를 t로 선언
s = turtle.Screen()          #그림 그려지는 화면 얻음
s.bgcolor("black")

def draw_star(aturtle, colour, side_length, x, y):      #draw_star(aturtle, colour, side_length, x, y)함수 선언
 t.color(colour)
 t.begin_fill()            #도형안에 색깔을 칠하기 위해 준비
 t.penup()               #거북이가 이동할 때 선 생기지 않음
 t.goto(x, y)               #좌표 (x, y) 이동
 t.pendown()             #거북이 이동할 때 선 생김
 for i in range(5):           #5번 반복
  t.forward(side_length)         #(side_length) 전진 
  t.right(144)                  #오른쪽으로 144도 회전
  t.forward(side_length)       #(side_length) 전진
 t.end_fill()           #도형 안에 색깔 칠하고 종료

for i in range(20):         #20번 반복
 color = random.choice([ 'white', 'yellow', 'blue', 'skyblue', 'orange', 'green' ])    #컬러는 랜덤으로 사용됨
 side_length = random.randint(10, 100)
 x = random.randint(-200, 200)
 y = random.randint(-200, 200)
 draw_star(t, color, side_length, x, y)          #draw_star(aturtle, colour, side_length, x, y)함수 사용
