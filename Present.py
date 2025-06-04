#HosamaAdem
n=int(input())
f=list(map(int,input().split()))
dict={}
for i in range(n):
    m=f[i]
    dict[m]=i+1

for i in range(1,n+1):
    print(dict[i],end=" ")

