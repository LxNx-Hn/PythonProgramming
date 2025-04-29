#기말 678, 체크안해줌 <- 평균이 너무 올라감
#수업시간에 중요하다고 말해줄 예정
#오늘부터 수업방식 변경, 과제줄여줄께 <-중요한거만
#쉬는시간 - 공시해줌
#파이썬에서는 프로그램을 쪼개는 3가지방법(함수,객체,모듈)
#함수 - 일을 수행하는 코드의 덩어리
#블랙박스 <- 입력값을 넣으면 결과값을 내주는 것
#스택구조로 호출

#함수의 다양한 형태
""" #매개변수가 없는, Void형태 함수
def print_test():
    print("test")
#매개변수 포함, Void형태 함수
def print_test2(name):
    print(name)

def calc_area(radius:float):
    area= 3.14 * radius * radius
    return area
#flote형태 리턴
def sum(a, b):
    return a + b
#함수는 일급객체, 다른함수의 매개변수로 사용가능
area_sum=sum(calc_area(5.0), calc_area(10.0))
print(area_sum) """

""" def get_sum(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum    
a,b=map(int, input("정수 2개 입력: ").split())
print("합계:", get_sum(a, b)) """

""" import turtle
t = turtle.Turtle()
t.setx(-200)
t.sety(-200)
def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
draw_square(100)
draw_square(200)
draw_square(300)
draw_square(400)
turtle.done() """

""" def sort_num(a, b):
    if a > b:
        return b, a
    else:
        return a, b """
    
""" def calc(n1,n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2
n1, n2 = 200, 100 #다중할당
t1,t2,t3,t4 = calc(n1, n2) #동시할당
#다중할당: 여러개의 값을 한번에 할당하는 것
#동시할당: 여러개의 변수에 값을 한번에 할당하는 것
print("{}+{}={}".format(n1, n2, t1))
print("{}-{}={}".format(n1, n2, t2))
print("{}*{}={}".format(n1, n2, t3))
print("{}/{}={}".format(n1, n2, t4)) """

#지역변수와 전역변수
""" def print_count():
        global temp
        count = 0
        temp = 0
        print("temp:",temp)
        print("count:", count)
count = 100
temp= 500
print_count()
print("temp:",temp)
print("count:", count) """
#전역변수의 사용은 최소화 해야함

#디폴트인자
""" def order(num,pickle=True,onion=True):
    print("햄버거={}개, 피클={}, 양파={}".format(num, pickle, onion))
order(2)
#매개변수를 다 지정하지않아도 기본값을 사용함
#키워드인자, 위치인자가먼저와야함
order(3,True, pickle=False) """
""" import turtle
t=turtle.Turtle()
t.speed(0)
def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360/n)
for i in range(50):
    t.left(10)
    n_polygon(6, 100)
turtle.done() """
#재귀함수 - 로직돌리기가 시험에 나옴
""" def pibo(n):
    if n<=2:
        return n
    return pibo(n-1) + pibo(n-2)
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1) """
#모듈 : 함수, 클래스, 변수 등을 모아놓은 파일
#각 모듈은 독립적으로 존재하며, 다른 모듈에서 import하여 사용할 수 있음
""" import datetime
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(datetime.datetime.now()) """
#함수/모듈/객체
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.forward(100)
s=turtle.Turtle()
s.shape("square")
s.backward(100)
turtle.done()