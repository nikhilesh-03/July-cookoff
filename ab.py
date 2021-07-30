import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    
    if b%a == 0 or a%b == 0:
        print(0)
    elif math.gcd(a,b) != 1:
            print(0)
    elif a%2 == 0 and b%2 == 0:
        print(0)
    
    elif a%2 !=0 and b%2 != 0:
        
        
        if math.gcd(a+1,b) != 1:
            print(1)
        elif math.gcd(a,b+1) != 1:
            print(1)
        else:
            print(2)
    else:
        print(1)