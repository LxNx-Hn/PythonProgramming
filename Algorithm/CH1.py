#선택정렬 알고리즘
#선택정렬 알고리즘은 배열을 순회하면서 최소값을 찾아서 맨 앞에 있는 값과 바꾸는 방식으로 정렬한다.
""" array=[9,8,7,6,5,4,3,2,1,0] #길이는 10
def selection_sort(array):
	n = len(array)
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] =  array[min_index], array[i]
		print(array[:i+1])#정렬과정을 보기위해 추가한 코드, 최소값을 찾아서 바꾸는 과정을 보여준다.

print("before: ",array)
selection_sort(array)
print("after:", array) """
#배열의 길이가 N일때 N-1번의 비교를 해야한다.
#n(n-1)/2 = n^2/2 - n/2
#따라서 시간복잡도는 O(N^2)이다.
#최악의 경우는 배열이 역순으로 정렬되어있을때이다.
""" def recursive_sort(array):
    if len(array) <= 1:
        return array

    avg = sum(array) / len(array)
    left = [x for x in array if x < avg]
    right = [x for x in array if x >= avg]
    print(left,right)
    return recursive_sort(left) + recursive_sort(right)

array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("before:", array)
sorted_array = recursive_sort(array)
print("after:", sorted_array) """
#O(nlogn)
""" i=3
print(f"{i}") """
#파이썬의 f스트링, 따옴표안에 f를 붙이면 중괄호안에 변수를 넣을 수 있다.
a=list(range(3,5))
b=range(1,5)
print(type(a))
print(a)