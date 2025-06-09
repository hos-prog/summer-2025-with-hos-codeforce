#HosamaAdem
n,x=map(int,input().split())
j=0
for i in range(n):
    h,m=input().split()
    m=int(m)
    if h=="+":
        x=x+m
    elif h=="-" and x>=m:
        x=x-m
    else:
        j+=1
print(x,j)
