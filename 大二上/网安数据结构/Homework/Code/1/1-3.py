class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class linkNode():
    def __init__(self):
        self.head=Node()
        self.length=0
    def isEmpty(self):
        return self.length==0
    def add(self,value):
        newnode=Node(value,self.head)
        self.head=newnode
        self.length+=1
    def append(self,value):
        newnode=Node(value)
        if self.isEmpty():
            self.head=newnode
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=newnode
        self.length+=1
    def delete(self,value):
        current=self.head
        if self.head.value==value:
            if self.length==1:
                self.head=None
            else:
                while current.next!=self.head:
                    current=current.next
                current.next=self.head.next
                self.head=self.head.next
            self.length-=1
        while current.next!=self.head:
            if current.next.value==value:
                current.next=current.next.next
                self.length-=1
                break
            current=current.next
    def f(self):
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=self.head
l=linkNode()
s=input()
s=s.split(',')
N=int(s[0])
M=int(s[1])
for i in range(N):
    l.append(i+1)
l.f()
x=1
ans=list()
while l.length>0:
    current=l.head
    while current.value!=x:
        current=current.next
    for i in range(M):
        current=current.next
    x=current.next.value
    ans.append(current.value)
    l.delete(current.value)
print(','.join(map(str, ans)))