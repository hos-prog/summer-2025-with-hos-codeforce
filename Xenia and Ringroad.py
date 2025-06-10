#HosamaAdem
n,m=list(map(int,input().split()))
g=list(map(int,input().split()))
home=1
time=0
for i in range(m):
    if home<=g[i]:
        time+=g[i]-home
        home=g[i]
    elif home>g[i]:
        time+=n-(home-g[i])
        home=g[i]
print(time)

