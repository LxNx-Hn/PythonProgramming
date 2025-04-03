n=int(input("정수를 입력하세요: "))
for i in range(1,2*n):
    j=n-i
    k=2*i-1
    if i <= n:
        print(" "*j,"*"*k,sep="")
    else:
        j=i-n
        k=2*(n-j)-1
        print(" "*j,"*"*k,sep="")