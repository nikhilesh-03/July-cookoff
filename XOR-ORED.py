#Question4
for _ in range(int(input())):
    n=int(input())
    li=list(map(int, input().split( )))
    p=max(li)
    a=0
    for i in range(len(li)):
        k=li[i]^p
        a=k|a
    print(p)
    print(a)
