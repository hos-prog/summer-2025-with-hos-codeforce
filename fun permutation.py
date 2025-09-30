#hos 
import sys
input=sys.stdin.readline
t=int(input())

for _ in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    bim=[n-i+1 for i in a]
    print(*bim)

