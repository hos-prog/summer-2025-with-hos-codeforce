#hos
n, k, l, c, d, p, nl, np=map(int,input().split())
over_all=(k*l)//nl
limes=c*d
salt=p//np
toasts=min(over_all,limes,salt)//n
print(toasts)
