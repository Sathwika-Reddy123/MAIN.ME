l=list(map(int,input().split(',')))
k=int(input())
t=[]
r=[]
i,j=0,0
while(j<len(l)):
    while((len(t)!=0) and (l[j]<t[-1])):
        t.pop(-1)
    t.append(l[j])
    if(j-i+1==k):
        r.append(t[0])
        if(l[i]==t[0]):
            t.pop(0)
        i=i+1
    j=j+1
print(*r)
