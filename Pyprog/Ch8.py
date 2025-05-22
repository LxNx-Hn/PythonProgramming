#12일 기말고사, 6일 미프마감
#DICTIONARY
#A dictionary is a collection of key-value pairs
#A set is a collection of unique elements
#A dictionary is mutable, while a set is unordered and mutable
#A dictionary is indexed by keys, while a set is indexed by its elements
#A dictionary can have duplicate keys, while a set cannot have duplicate elements
#A dictionary can have any data type as a key, while a set can only have immutable data types as elements
#키/밸류/두개같이 가져오는 메소드 익히기
#SET
#LAB 8-1
#편의점 재고 관리 프로그램
""" Stock = {"커피음료": 7 ,"펜":3,"종이컵":2, "우유": 8,"콜라":4,"책":5}
while True:
    SearchItem = input("재고를 확인할 품목을 입력하세요: ").lower()
    if SearchItem == "q":
        break
    if SearchItem in Stock:
        print("재고 수량은{}개 입니다.".format(Stock.get(SearchItem)))
    else:
        print("재고가 없습니다.") """
#8-2 나올수있는 모든 결과 체크
""" print("사전프로그램")
dict = {}
while True:
    st = input("$ ")
    command = st[0]
    if command == "<": 
        st = st[1:]
        inp = st.split(":")
        if len(inp) < 2:
            print("잘못된 입력입니다.")
        else:
            dict[inp[0].strip()] = inp[1].strip()
    elif command == ">":
        st = st[1:]
        inp = st.strip()
        if inp in dict:
            print(dict[inp])
        else:
            print("{}가 사전에 없습니다.".format(inp))
    elif command == "q":
        break
    else:
        print("잘못된 입력입니다.")
print("사전 프로그램을 종료합니다.") """
#8-3
""" partyA=set(["park", "kim", "lee"])
partyB=set(["park", "choi"])
print("2개의 파티에 참석한 사람들")
print(partyA.intersection(partyB))
print("파티 A,B에 참석한 사람들")
print(partyA.union(partyB))
print("파티 A,B에 중복없이 참석한 사람들")
print(partyA.symmetric_difference(partyB))
print("파티A에만 참석한 사람들")
print(partyA.difference(partyB))
print("파티B에만 참석한 사람들")
print(partyB.difference(partyA)) """
#8-4
#파일에서 사용된 단어 구하기
def process(w):
    output = ""
    for ch in w:
        if ch.isalpha():
            output += ch
    return output.lower()
words = set()
fname = input("파일 이름을 입력하세요: ")
f = open(fname, "r")
for line in f:
    lineWords = line.split()
    for word in lineWords:
        words.add(process(word))
print("파일에 사용된 단어의 수는 {}개 입니다.".format(len(words)))
print(words)