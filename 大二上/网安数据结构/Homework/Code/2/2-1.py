inp=input()
t=[]
s=[]
ans=[]
dic={')':'(',']':'[','}':'{'}
s.append('#')
for c in inp:
    if c in ['[','{','(']:
        s.append(c)
    elif c in [']','}',')']:
        if dic[c] == s[-1]:
            s.pop()
        else:
            t.append(c)
if '(' in s or ')' in t:
    ans.append(1)
if '[' in s or ']' in t:
    ans.append(2)
if '{' in s or '}' in t:
    ans.append(3)
if len(ans)>0:
    for n in ans:
        print(n,end=",")
    print('')
else:
    print(0)