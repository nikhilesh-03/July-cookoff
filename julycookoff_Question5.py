#Question5
for _ in range(int(input())):
    n=int(input())
    li=list(map(int, input().split( )))
    p=min(li)
    count=0
    bool=True
    for t in range(len(li)):
        if li[t]==p:
            count+=1

    for i in range(len(li)):
        if li[i]!=p:
            if li[i]%(li[i]-p)!=p:
                bool=False
                break
            else:
                pass
        else:
            pass
    if bool:
        print(len(li)-count)
    else:
        print(len(li))

