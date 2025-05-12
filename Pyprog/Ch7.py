#7.List
#LIST: Variable = [1,2,3,4,5] 형태로 선언, 데이터 타입이 자유로움
""" Web=[]
Web=list()
Web=['huggingface','tensorflow','pytorch'] """
#in, not in 연산자 사용 가능
""" print('tensorflow' in Web)
print('huggingface' not in Web) """
#리스트의 길이 len()함수 사용
#리스트에 요소를 추가하는법
""" Web.append('keras') #리스트에 요소 추가 1
Web.insert(1,'fastai') #리스트에 요소 추가 2
Web.extend(['scikit-learn','numpy']) #리스트에 요소 추가 3
Web = Web + ['pandas'] #리스트에 요소 추가 4 -다형성
LIST=list(range(1,11)) #형태도 가능 """
#리스트의 요소 접근
""" print(Web[0])
print(Web[1:])
 """
#리스트 에서의 연산자 사용
""" num1=[10,20,30]
num2=[40,50,60]
number=num1+num2 #리스트 결합
print(number)
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) 
num_list=[0,1,2]*3
print(num_list) #리스트 반복 """
#리스트에서의 함수
""" student=[['kim',178.9],['park',175.3],['lee',180.5]]
print(type(student))
#map(A,B): A의 각 요소에 B를 적용
t_list=list((10,20,30))#캐스팅, 튜플을 리스트로 변환
a_list=[10,20,30]
b_list=[0,10,20,30]
c_list=[0,""]
print(any(a_list))
print(any(b_list))
print(any(c_list))
print(all(a_list))
print(all(b_list))
print(all(c_list)) """
#any(): 리스트의 요소가 하나라도 True이면 True
#all(): 리스트의 요소가 모두 True이면 True
#인덱싱과 슬라이싱
""" list=[1,2,3,4,5]
print(list[0]) #인덱싱
print(list[-1])#음수를 이용해 역방향접근도 가능
print(list[1:3]) #슬라이싱 """
#기타 함수들
""" List=[1,2,3,4,5]
print(List.count(1)) #리스트에서 1의 개수
print(List.index(1)) #리스트에서 1의 위치
print(List.pop(0)) #리스트에서 0번째 요소를 삭제하고 반환
print(List) #삭제 후 리스트
print(reversed(List)) #리스트를 역순으로 반환
print(sorted(List)) #리스트를 정렬하여 반환 """
#193p.
""" population=['seoul',9765,'busan',3441,'incheon',2954]
print("서울인구:",population[1])
print("인천인구",population[-1])
print("도시리스트",population[::2])
print("인구의합:",sum(population[1::2])) """
#삭제
""" LIST=[1,2,3,4,5]
LIST.remove(1) #리스트에서 1을 삭제
print(LIST)
LIST.clear() #리스트를 비움
print(LIST)
LIST=[1,2,3,4,5]
LIST.pop() #리스트에서 마지막 요소를 삭제
print(LIST)
LIST=[1,2,3,4,5]
del LIST[0] #리스트에서 0번째 요소를 삭제
print(LIST)
del LIST #리스트를 삭제
print(LIST) #삭제된 리스트를 출력하면 오류 발생 """

""" num_list=[1,2,3,4,5]
print(num_list.index(3)) #리스트에서 3의 위치
print(num_list.count(3)) #리스트에서 3의 개수
for i in num_list:
    print(i) #리스트의 요소를 하나씩 출력 """
#정렬
""" num_list=[2,6,3,123,62,2,9,213,1,2]
sorted_list=sorted(num_list) #리스트를 정렬하여 반환 - 함수
print(sorted_list) #정렬된 리스트 출력
num_list.sort(reverse=True) #리스트를 정렬 - 메소드
print(num_list) #정렬된 리스트 출력 """
#문자도 ㄱㄴㄷ, abc 순으로 정렬됨
""" s= "py th,on"
string_list=list(s) #문자열을 리스트로 변환
print(string_list) #리스트 출력 """
#split()함수 : ()안에 있는 문자로 문자열을 나누어 리스트로 변환
""" s= "py,th,on"
string_list=s.split(",") #문자열을 리스트로 변환
print(string_list) #리스트 출력 """
""" city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]
max_pop=0
min_pop=9999
total_pop=0
for city in city_info:
    total_pop+=city[1]
    if city[1]>max_pop:
        max_pop=city[1]
        max_city=city
    if city[1]<min_pop:
        min_pop=city[1]
        min_city=city
print('최대인구:{}, 인구{}천명'.format(max_city[0],max_city[1]))
print('최소인구:{}, 인구{}천명'.format(min_city[0],min_city[1]))
print('평균인구 {}천명'.format(total_pop/len(city_info))) """

#zip()함수 : 여러 개의 리스트를 묶어주는 함수
#A,B=zip(*LIST) 형태로 풀기도 가능
""" city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]
city_name, city_pop = zip(*city_info) #zip()함수 사용
max_pop=max(city_pop)
print("최대인구수",max_pop)
n=city_pop.index(max_pop)
print("최대인구수 도시{}, 인구{}천명".format(city_name[n],max_pop))
min_pop=min(city_pop)
n=city_pop.index(min_pop)
print("최소인구수 도시{}, 인구{}천명".format(city_name[n],min_pop))
print("평균인구수",sum(city_pop)/len(city_pop))
 """
#내부 max,min함수도 복잡도가 O(n)이다.
#immutable한 자료형 : 튜플, 문자열, 세트(집합)
#튜플은 리스트에비해 접근 속도가 빠르다.
#mutable한 자료형 : 리스트, 딕셔너리
#객체와 클래스, 인스턴스의 차이 <- 기말고사에 나옴

#리스트 컴프리헨션 : 리스트를 간단하게 생성하는 방법
#리스트를 생성할 때 for문을 사용하여 간단하게 생성하는 방법
[x**2 for x in range(1,6)] #1~10까지의 제곱수를 리스트로 생성
#[리스트 요소 for 반복문]