t=int(input())
for x in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d=dict.fromkeys(l,int(0))
    for i in l: # i--> element in l
        d[i]+=1
    print(d)
    s=list(d.keys())
    cnt=list(d.values())
    sum=0
    for i in range(0,len(s)):
        if(cnt[i]<s[i]):
            sum+=cnt[i]
        else:
            sum+=(s[i]-1)
    print(sum)
