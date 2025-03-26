#파이썬의 변수
#변수 : 값을 저장할때 사용하는 식별자
#변수선언 : pi=3.1415926535897977245485.... (변수생성)
#변수 할당 : print(pi) (변수에 값할당)
#변수참조 : >>3.14 (번수에서 값을 꺼냄)
#정수(int),실수(float),문자열(str)... 할당가능
""" a=int(1234)
b=float(3.14)
c=str("str")
print(a,b,c, sep=",")
print(type(a)) """ #타입확인가능 타입에러 발생시 타입확인하기
#식별자 : 프로그래밍 언어에서 이름을 붙일때 사용하는단어, 변수 또는 함수의 이름으로 사용
# 키워드 사용불가, 특수문자는 _만 허용, 숫자로 시작하면 사용불가,공백을 포함할수없음
""" import keyword
print(keyword.kwlist) """
#키워드 클래스안에 있는 키워드 확인가능
#print는 키워드가 아니지만, 만약 이를 변수로 사용해 할당한다면 더이상 출력기능을 하지못함 (메소드 오버라이딩)
#저런함수 판별법 -> 쳐봤는데 색깔나오면 이미 정의된 함수임
#변수 이름은 변수가 담고있는 내용을 한눈에 알수있게 지어야편하다
# 클래스명은 대문자시작 명사, 메소드명은 소문자시작 동사, 여러개의 단어를 사용할때는 camel case{카멜케이스(각단어의 시작은 대문자로) }사용하기



# **2 ->제곱계산법
# 파이썬은 / 연산자 사용시 자동으로 실수로 처리해준다
# a = int(input(---)) 변수안에 n타입을 저장 --- =입력받을떄 출력할 문구 // 타입기본은 문자열
""" name = input("이름을 입력하세요")
age =  input('나이를 입력하세요')
mail=input('메일을입력하세요')
print(name,age,mail)
 """
#두수를 입력후 +-연산출력프로그램
#cmd+[,]= 왼쪽, 오른쪽 들여쓰기
""" print("두정수의 합과 차를 구하는 프로그램입니다")
try:
    num1=int(input("첫번째 수 입력 : "))
    num2=int(input("두번째 수 입력 : "))
except ValueError:
    print("정수를 입력해주시기 바랍니다")
else:
    sum=int(num1+num2)
    sub=num1-num2
    print("두 정수의 합=",sum,sep="",end='')
    print("  두 정수의 차=",sub,sep='') """
#여기서 sum의 타입을 int로 지정할때 int(sum)형태로 감싸면 왜 안될까....
#int() - 괄호안의 자료 형변환 , 따라서 int(sum)에서 sum안에 자료가 없기때문에 에러가 난다
#int 지정법 -> 변수 선언 = 자료형()
#sum = int(sum) <- 자료형변경 예시
#a : int =3 <-자료형 설정법
""" math = int(input('수학점수를 입력하세요'))
eng  = int(input("영어점수를 입력하세요"))
avg  = float((math+eng)/2)
print("평균은 {:.1f}점 입니다".format(avg)) """
#cmd + opt ^ 커서 줄 늘리기(여러줄 선택할때 좋음)
""" hour=int(input("시 입력 : "))
min=int(input("분 입력 : "))
sec=int(input("초 입력 : "))
total=hour*3600 + min*60 +sec
print(total) """
#리스트버전
#a, b=input().split() 처럼 쓰면 cin<<과 비슷하게 사용가능함.
""" HMS=input("시,분,초 입력")
HMS=HMS.split()
hour=int(HMS[0])
min=int(HMS[1])
sec=int(HMS[2])
total=hour*3600 + min*60 +sec
print(total) """
""" celcius =float(input())
farenheit=celcius*1.8+32
print("{:.2f}°F".format(farenheit)) """
#celcius : float로 변수정의를 하면 왜 아래쪽에서 에러가 뜰까..
#celcius:float=input() <- 실수형 선언후 스트링값을 집어넣었기때문?
#파이썬에서는 자료형지정이 완벽하지않아서, 실수로 선언했지만 스트링값을 넣으면 스트링값이 된다.
#파이썬에서 .2f등으로 소수점 자리를 줄이면 반올림한다

#세자리수입력후 각 자리수 출력
""" num=int(input())
num1 = num%10
num2 = num%100
num3 = num%1000
print("{}".format(num1))
print("{}".format(num2))
print(num3)
print(num1)
print(num2//10)
print(num3//100) """
# // =몫 , %=나머지 , / = 실수형태로 나누기 
""" def birth():
    try:
        birth=int(input()) #00000000
    except ValueError:
        print('유효한 값을 입력해주세요')
    else:
        if birth>=10000000 and birth<=99999999:
            year= birth//10000
            day=birth%100
            month=(birth%10000)//100
            print(year,month,day)
        else:
            print('유효한 값을 입력해주세요')
birth() """
#기준점을 잡고 몇으로 나눌지 정한뒤 왼쪽값=// 오른쪽값= %
#p50
#height,weight = map(float,input("키와 뭄무게를 순차적으로 입력하세요>>").split())
""" height,weight = 170 , 45
bmi=weight/(height/100)**2
print("BMI>>{:.2f}".format(bmi)) """
#연산문제
""" a=2 
b=3
x=4 
y=(x**2)+((b*x)/a)+(b/(2*a))**2
print(y)
 """
#2-3
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
radius=100
t.circle(radius)
radius=200
t.circle(radius)
turtle.done() """
#52p 2.2
#71p 2.5, 2.9, 2,10, 2.11
#2.5
""" leng=int(input("정사각형의 밑변을 입력하시오>>"))
area=leng*leng
print("정사각형의 면적={}".format(area)) """
#2.9
""" Celcius=float(input("섭씨온도를 입력하시오>>"))
Fahrenheit=Celcius*1.8+32
print("섭씨{}도는 화씨{}도 입니다".format(Celcius,Fahrenheit)) """
#2.10
""" radius=float(input("원의 반지름을 입력하시오>>"))
PI=3.141592
area=PI*radius*radius
circumference=2*PI*radius
print("원의 둘레= {}, 원의 넓이= {}".format(circumference,area)) """
#2.11
# print("""It's really hot!
# I said "Hello" to him.
# He said "What's there?"
# Newline character is "\\n", Tab character is "\\t".
#  Working directory is "C:\\workspace\\mywork. """)
#print("It's really hot! \nI said \"Hello\" to him.\nHe said \"What\'s there?\" \nNewline character is \\n, Tab character is \\t.\nWorking directory is \"C:\\workspace\\mywork.")
#69p 
#52p 2.2
""" import turtle
t=turtle.Turtle()
t.shape("turtle")
for _ in range (4):
    radius=50
    for _ in range(3):
        t.circle(radius)
        radius*=2
    t.left(90)
turtle.done() """

#2.11
#주관식 문제
#2.1 (변수)는 컴퓨터의 메모리 공간에 이름을 붙이는 것으로 여기에 정수, 실수, 문자열 등의 자료값을저장할 수 있다.
#2.2 파이썬의 = 연산자는 '같다'는 등호의 의미가 아니라 '느 연산자 오른쪽의 값을 왼쪽의 변수에 저장하라는 의미이다. 이 연산자=를 (대입연산자) 혹은 (할당연산자)라고 한다.
#2.3 파이썬에서는 x,y= 100. 200과 같이 한 줄에 여러 개의 변수를 선언하고 이 변수에 값을 동시에 할당 할 수도 있는데, 이를 (동시할당문)이라 한다.
#2.4 변수의 이름은 (식별자)의 일종이다. "홍길동" "김철수" 등의 이름이 사람을 구별하듯이 (식별자)는 변수와 변수들을 구별하는 역할을 한다.
#2.5 파이썬은 미리 기능을 정의해 둔 코드를 필요에 따라 편리하게 호출하여 사용할 수 있다. 이와 같이 프로그래밍 언어에서 미리 정의한 기능을 (예약어)라고 한다.
#2.6 컴퓨터의 데이터는 그림과 같이 컴퓨터에 있는 핵심적인 부품인 메인 메모리에 저장된다. 이렇게 메모리에 데이터를 저장한 곳의 위치를(메모리주소)라고 한다.
#2.7 프로그램에서 사용할 수 있는 데이터의 종류를 (자료형)이라고 한다.
#2.8 파이썬에서 사용할 수 있는 가장 단순한 기본 자료형은 4가지 종류가 있다. 첫 번째는 1이나 2와 같은 (정수)이다. 두 번째는 3.14와 같은 (실수)이다. 세 번째는 'Hello'와 같은 (문자열)이다. 마지막으로 네 번째는 참과 거짓을 나타내는 (부울)형이다.
#2.9 파이썬에서 변수의 자료형을 알려면 변수의 이름에 (type()) 함수를 적용하면 된다.
#2.10 객체 +.+ 명령 형식의 구조에서 객체가 . 연산자로 구분된 명령을 내릴 때 이 명령을 (메소드)라고 부른다.
#2.11 변수는 수학에서 유래한 개념이다. 수학에서 변수는 변할 수 있는 양을 표현하기 위해 사용되는 기호이다. 이 기호는 하나의 특정한 값이 아니라 허용되는 모든 값을 표현하기 위해 사용된다. 이와 상대되는 개념이(상수)이다. (상수)는 값이 고정되어 있는 수이다.