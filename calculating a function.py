#HosamaAdem
n=int(input())
t=0
'''
for i in range(1,n+1):
    if i % 2 != 0:
        t-=i
    else:
        t+=1
'''
'''
the above code gets time limit exceed when you put 1 billion (1,000,000,000) it doesn't work
 so there is a formula that can do this alteranting sum from 1 to n
 if n is even n/2 ,if n is odd -n+1/2
'''
if n % 2 == 0:
    print(n//2)
else:
    print(-(n+1)//2)

#this code has time limit O(1)
