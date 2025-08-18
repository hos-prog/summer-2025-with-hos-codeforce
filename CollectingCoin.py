
#hos
t=int(input())
for _ in range(t):
    a,b,c,n=map(int,input().split())
    the_max=max(a,b,c)
    need=0
    if the_max!=a:
        need+=(the_max-a)
    if the_max!=b:
        need+=(the_max-b)
    if the_max!=c:
        need+=(the_max-c)
    if need>n:
        print("NO")
    elif (n-need)%3==0:
        print("YES")
    else:
        print("NO")
