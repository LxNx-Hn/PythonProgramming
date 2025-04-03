#반복문이지않을까요
#제어구조 3가지 : 순차 조건 반복, 교재내부 파란 키워드 위주로 공부하기
""" for i in "range":
    print("#"*20) """
#LAB1
#for문
""" import turtle
t=turtle.Turtle()
for i in range(6):
    t.circle(100)
    t.left(360/6)
turtle.done() """
#while문
""" import turtle
t=turtle.Turtle()
i=0
while i<6:
    t.circle(100)
    t.left(360/6)
    i+=1
turtle.done() """
#LAB2
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
for i in range(3):
    t.forward(100)
    t.left(360/3)
t.penup()
t.goto(200,0)
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(360/4)
turtle.done() """
#while문 버전
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
i=0
while i<3:
    t.forward(100)
    t.left(360/3)
    i+=1
t.penup()
t.goto(200,0)
t.pendown()
i=0
while i<4:
    t.forward(100)
    t.left(360/4)
    i+=1
turtle.done() """
#LAB3
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput("","몇각형을 원하시나요?:")
n=int(s)
for i in range(n):
    t.forward(100)
    t.left(360/n)
turtle.done() """
#while문 버전
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput("","몇각형을 원하시나요?:")
n=int(s)
i=0
while i<n:
    t.forward(100)
    t.left(360/n)
    i+=1
turtle.done()  """
#LAB4
""" n=int(input("정수를 입력하시오: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("{}!은 {}입니다.".format(n,fact)) """

""" n=int(input("정수를 입력하시오: "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print("{}!은 {}입니다.".format(n,fact)) """

#p.150 심화문제 5.2(1)
#for 버전
""" sum=0
for i in range(100):
    if i%2!=0:
        sum+=i
print("1부터 100까지의 홀수의 합은 {}입니다.".format(sum)) """
#while 버전
""" sum=0
i=1
while i<100:
    sum+=i
    i+=2 
print("1부터 100까지의 홀수의 합은 {}입니다.".format(sum))"""
#심화 5.4
""" n= int(input("숫자를 입력하세요"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",sep="",end="")
    for j in range(i):
        print("*",sep="",end="") 
    print() """
    
#심화 5.10
""" import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.width(2)
for _ in range(30):
    num = random.randrange(2)
    if num == 0:
        t.right(90)
        t.forward(50)
    else:
        t.left(90)
        t.forward(50)
turtle.done()  """
#심화 5.4 마름모
""" n=int(input("정수를 입력하세요: "))
for i in range(1,2*n):
    j=n-i
    k=2*i-1
    if i <= n:
        print(" "*j,"*"*k,sep="")
    else:
        j=i-n
        k=2*(n-j)-1
        print(" "*j,"*"*k,sep="") """
#5.4마름모 액자
""" n=int(input("정수를 입력하세요: "))
for i in range(1,2*n):
    j=n-i
    k=2*i-1
    if i <= n:
        print("*"*j," "*k,"*"*j,sep="")
    else:
        j=i-n
        k=2*(n-j)-1
        print("*"*j," "*k,"*"*j ,sep="") """
#중간문제 ,continue, break 한문장안에서 구분하기
#ipo <- input process output 중간문제에서나옴