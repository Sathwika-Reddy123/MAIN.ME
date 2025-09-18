l=list(map(int,input().split(',')))
k=int(input())
t=[]
r=[]
i=0
j=0
while(j<len(l)):
    while((len(t)!=0) and (l[j]<t[-1])):
            t.pop(-1)
    if(l[j]<0):
        t.append(l[j])
    if(j-i+1==k):
        if(len(t)==0):
            r.append(0)
        else:
            r.append(t[0])
        if(len(t)>0 and l[i]==t[0]):
            t.pop(0)
        
            
        i=i+1
    j=j+1
print(*r)
