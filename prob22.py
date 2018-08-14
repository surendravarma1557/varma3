j,k,l=map(int,input().split())
s=0
for i in range(1,j+1):
	s=s+(k+(i-1)*l)
print(s)	
	
