n=int(input())
l=list(map(int,input().split()))
l.sort()
s=0
j=1
k=[]
for i in range(n):
	h=l.count(l[i])
	if h==1:
		k.append(l[i])
		s=s+1*j
		j=j+1
	elif h>1 and l[i] not in k:
		s=s+h*j
		k.append(l[i])
		j=j+1
print(s)	
