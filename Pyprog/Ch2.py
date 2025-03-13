#Desc: Python Programming, 2nd ed.
#p28. print()
#파이썬의 표춘 출력함수 print()
#출력 : 자동개행
#문자열 출력시에는 "" or ''로 문자열 감싸기
#파이썬의 f스트링, 따옴표안에 f를 붙이면 중괄호안에 변수를 넣을 수 있다.
#sep = ,사이에 들어가는 간격 설정 -> 기본은 " "
#end = 끝날때 출력할 문자 -> 기본은 \n(escape sequnce)

#42p연습문제 1.3 1.4 1.5 1.6
#1.3
""" print(100)
print(100+200)
print('100+200')
print(100,200)
print('100','200')
print('100''200')
print("Hello Python!")
print("Hello","Python","!")
print("Hello"+"Python"+"!")
print("Hello""Python""!")
print('***************')
print('*'*28) """
#1.4
""" print("Hello Python!")
print('*'*20)
print(Life is short learn Python) #문자열을 ''없이 출력하면 생기는 문제, 공백이 없을시 변수처리가되어 오류는 발생하지않음
print(100+'200')#문자열과 정수를 연산하려고 하면 생기는 문제, int("200") 등으로 변환해줘야함 """
#1.5
""" for _ in range(5):
    print("i love python") """
#1.6
""" for i in range(7):
    print("*"*i) """
#1.7
""" import turtle

t = turtle.Turtle()
t.forward(100)
t.left(135)
t.forward(141.4) 
t.left(135)
t.forward(100)
turtle.done() """

""" import turtle
t = turtle.Turtle()
for _ in range(3):
    t.forward(100) 
    t.left(120) 
t.left(120)
for _ in range(2):
    t.forward(100) 
    t.right(120)
turtle.done() """
#1.9
""" print(400-200+100)
print(409*200-100)
print(6*3/9)
print(9**3)
print(9/3)
print(9//3) """
#1.12
""" def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print("3! =",fact(3))
print("4! =",fact(4))
print("5! =",fact(5))
print("6! =",fact(6))
print("7! =",fact(7)) """
#파이썬은 동적타입언어이다. 변수의 타입을 지정하지 않아도 된다.
#파이썬의 operator
#산술연산자 : +, -, *, /(실수로나누기), //(몫), %(나머지), **(제곱)
#비교연산자 : ==, !=, >, <, >=, <=
#논리연산자 : and, or, not
#비트연산자 : &, |, ^, ~, <<, >>

#터틀 그래픽
#python -m turtledemo #데모그래픽 확인 명령

""" import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
turtle.bgcolor("black")

def Geo(n):
    for _ in range(n):
        t.forward(100)
        t.right(360/n)

# 삼각형 그리기
t.color("red")
Geo(3)
# 사각형 그리기
t.color("blue")
Geo(4)
# 오각형 그리기
t.color("green")
Geo(5)
# 육각형 그리기
t.color("yellow")
Geo(6)
# 칠각형 그리기
t.color("purple")
Geo(7)
# 팔각형 그리기
t.color("orange")
Geo(8)
turtle.done() """

#print("Hello Python!")
""" 반지름=4
PI=3.141592
면적=반지름**2*PI
print(면적) """
""" import numpy as np 
x = np.random.randint(0, 10, size=10)
print(x)
print(np.sort(x)) """