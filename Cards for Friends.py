#hos
t=int(input())
for _ in range(t):
    w,h,n=map(int,input().split())
    shets=1
    while w%2==0:
        w//=2
        shets*=2
    while h%2==0:
        h//=2
        shets*=2
    print("YES" if shets >=n else "NO")  
    
    