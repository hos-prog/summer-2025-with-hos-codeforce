#hos
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(n)
    summ=[]
    for i in range(len(s)):
        if s[i]!="0":
            zeros=len(s)-(i+1)
            m=s[i]+zeros*"0"
            summ.append(int(m))
    print(len(summ))
    print(*summ)


