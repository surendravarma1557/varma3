n=int(input())
if(n<=1000):
    stg=input()
    stg=[int(x) for x in stg.split()]
    k=sorted(stg[0:n])
for i in range(0,n):
    if(i<n-1):
        kk=' '
    else:
        kk=' '
    print(k[i],end=kk)    
