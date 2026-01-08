s1=input()
s2=input()
s=set()
for c in s2:
    s.add(c)
for c in s1:
    if c not in s:
        print(c,end="")