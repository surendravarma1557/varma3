a=input()
m1=0
m2=0
new=[]
o_list=[int(x) for x in input().split()]
s=len(o_list)
while(m1==0):
    l=o_list[m1]
    o_list.remove(o_list[0])
    if((l in o_list)and(l not in new)):
        print(l,end=" ")
        new.insert(m2,l)
        n2+=1
    elif((o_list==new) and (l not in new) and (s==len(new))):
        print('unique')
    if(o_list==[]):
        break
