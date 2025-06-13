#Hosam Adem
n=int(input())
c=0
m=0
for i in range(n):
    mi,ci=map(int,input().split())
    if mi>ci:
        m+=1
    elif ci>mi:
        c+=1
if c>m:
    print("Chris")
elif c<m:
    print("Mishka")
else:
    print("Friendship is magic!^^")
# This code has a time complexity of O(n)
