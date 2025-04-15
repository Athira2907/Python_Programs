1) https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
l=[]
for i in range(len(s)):
    l1=[]
    temp=s
    temp=temp[i:]
    for j in range(len(temp)):
        l1+=[temp[:j+1]]
    l+=l1
l3=[i for i in l if i[0] not in 'AEIOU']
l4=[i for i in l if i[0] in 'AEIOU']
if len(l3)>len(l4):
    print('Stuart '+str(len(l3)))
elif len(l4) >len(l3):
    print('Kevin '+str(len(l4)))
else:
    print('Draw')



2) https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
if (year%4==0 and year%100!=0) or year%400==0:
        leap=True
    
    return leap

3) https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
l=[['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
l1=[l[i][1] for i in range(len(l))]
# print(l1)
l1=list(set(l1))
l1.sort()
# print(l1)
val=l1[1]
# print(val)
l2=[l[i][0] for i in range(len(l)) if l[i][1]==val]
l2.sort()
print(l2)

4) https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
l=[]
val=0
for i in range(k):
    l+=[s[val:val+k]]
    val+=k
l1=[]
for i in l:
    s1=''
    for j in i:
        if j not in s1:
            s1+=j
    l1+=[s1]
for i in l1:
    print(i)


5) https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
import math
AB=int(input())
BC=int(input())
AC=math.sqrt(AB**2 + BC**2)
MC=AC/2
BM=math.sqrt(BC**2 - MC**2)
MBC=(BM**2 + BC**2 - MC**2)/(2* BM *BC)
MBC=math.acos(MBC)
MBC=math.degrees(MBC)
MBC=round(MBC)
print(MBC)

6) https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
mn=input()
mn.strip()
m,num=int(mn[0]),int(mn[-1])
n=input()
l=n.split(' ')
A=input().split(' ')
B=input().split(' ')
happiness=0
for i in l:
    if i in A:
        happiness+=1
for i in l:
    if i in B:
        happiness-=1
print(happiness)


7) https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
n=int(input())
l=[input() for i in range(n)]
print(len(set(l)))
l2=[]
for i in l:
    if i not in l2:
        l2+=[i]
for i in range(len(l2)):
    print(l.count(l2[i]),end=' ')
-------
n=int(input())
l=[input() for i in range(n)]
print(len(set(l)))
res={}
for i in l:
    if i not in res:
        res[i]=1
    else:
        res[i]+=1
print(*res.values())


8) https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
s=input()
s=s+' '
s1=''
l=[]
for i in range(len(s)-1):
    s1+=s[i]
    
    if s[i]!=s[i+1]:
        l+=[s1]
        s1=''

l2=[(len(i),(int(str(i[0])))) for i in l]
for i in l2:
    print(i,end=' ')


9) https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
s=input()
l=list(s)
l.sort()
s=''.join(l)
s=s+' '
s1,l='',[]
for i in range(len(s)-1):   
    s1+=s[i] 
    if s[i]!=s[i+1]:
        l+=[s1]
        s1=''
l.sort(key=len,reverse=True)
res={}
for i in l:
    if len(i) not in res:
        res[len(i)]=[]
    res[len(i)]+=[i]
c,l1=0,[]
for i in res.values():
    l1.extend(i)
for i in l1:
    if c==3:
        break
    print(str(i[0])+' '+str(len(i)))
    c+=1

10) 
