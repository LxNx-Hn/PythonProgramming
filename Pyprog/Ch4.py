""" a, b = map(int, input("산술,비교연산자-두수를 입력하세요: ").split())
#산술연산
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)
#비교연산
print("a == b =", a == b)
print("a != b =", a != b)
print("a > b =", a > b)
print("a < b =", a < b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)
#논리연산
x, y = map(bool, input("논리연산자-두값을 입력하세요: ").split())
print("x and y =", x and y)
print("x or y =", x or y)
print("not x =", not x)
#비트연산
c, d = map(int, input("비트연산자-두값을 입력하세요: ").split())
bin(c), bin(d)
print("c & d =", c & d)
print("c | d =", c | d)
print("c ^ d =", c ^ d)
print("~c =", ~c)
print("c << 1 =", c << 1)
print("c >> 1 =", c >> 1)
#랜덤라이브러리
import random
print(random.random())
print(random.randint(1, 7))
print(random.randrange(7))
print(random.randrange(1, 7))
lst=[10,20,30,40,50]
print(lst)
random.shuffle(lst)
print(random.choice(lst)) """

#RFM 계산
""" GenderCode = bool(int(input("여성이면 1, 남성이면 0을 입력하세요: ")))
height, radius = map(float, input("키와 허리둘레를 입력하세요: ").split())
rfm = (76 if GenderCode else 64) - (20 * (height / radius))
print("당신의 RFM은 {:.4f}입니다".format(rfm))

rfm = (76 if bool(input("여성이면 1, 남성이면 0을 입력하세요: ")) else 64)-\
20 * (lambda h, r: h / r)(*map(float, input("키와 허리둘레를 입력하세요: ").split()))
print(f"당신의 RFM은 {rfm:.4f}입니다") """
#p104
""" import turtle
import random
import turtle
turtle.setup(width=400, height=400)
t = turtle.Turtle()
t.speed(0) 
turtle.bgcolor("black")
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]
for i in range(200):
    t.color(random.choice(colors)) 
    t.forward(i)
    t.left(93)
turtle.done() """
#4-1
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0,0)
t.pendown()
s=turtle.textinput("","정수를 입력하시오: ")
n=int(s)
if n>0:
    t.goto(100,100)
elif n==0:
    t.goto(100,0)
else:
    t.goto(100,-100)
turtle.done() """
4-3
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3,3)
while True:
    command=turtle.textinput("명령","명령을 입력하시오: ")
    if command=="l":
        t.left(90)
        t.forward(100)
    if command=="r":
        t.right(90)
        t.forward(100)
    if command == "h":
        t.shapesize(30, 30)
    if command == "n":
        t.shapesize(3, 3)
    if command == "f":
        t.forward(100)
    elif command.isdigit() and 1 <= int(command) <= 9: 
        size = int(command)
        t.shapesize(3 * size, 3 * size) 
    
    if command=="q":
        break
turtle.done() """

#4-8 도전
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput("","도형을 입력하시오: ")
if s=="사각형": 
    s=turtle.textinput("","가로: ")
    w=int(s)
    s=turtle.textinput("","세로: ")
    h=int(s)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
elif s=="삼각형":
    s=turtle.textinput("","변: ")
    w=int(s)
    t.forward(w)
    t.left(120)
    t.forward(w)
    t.left(120)
    t.forward(w)
    t.left(120)
elif s=="원":
    s=turtle.textinput("","반지름: ")
    r=int(s)
    t.circle(r)
else:
    t.write("사각형, 삼각형, 원 중 하나를 입력하시오.")
turtle.done() """

#4-9
""" import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
for _ in range(10):
    num = random.randrange(2)
    if num == 0:
        t.right(90)
        t.forward(50)
    else:
        t.left(90)
        t.forward(50)
turtle.done() """