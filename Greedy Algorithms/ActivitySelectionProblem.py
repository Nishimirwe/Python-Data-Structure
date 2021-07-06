
class activity:
    def __init__(self,act,start,end):
        self.act=act
        self.start=start
        self.end=end

class available:
    def __init__(self):
        self.num=0
        self.activities=[]

    def add(self,act,start,end):
        a=activity(act,start,end)
        self.activities.append(a)
        self.num+=1

    def show(self):
        for i in range(self.num):
            print(self.activities[i].act,":",self.activities[i].start,":",self.activities[i].end)
        print()

def canBeDone(av):
    allow=[av.activities[0]]
    print(av.activities[0].act,av.activities[0].start,av.activities[0].end)
    for i in range(av.num):
        if av.activities[i].start >= allow[0].end:
            allow[0]=[av.activities[i]]
            print(av.activities[i].act,av.activities[i].start,av.activities[i].end)

p=available()
p.add("A1",0,6)
p.add("A2",3,4)
p.add("A3",1,2)
p.add("A4",5,8)
p.add("A5",5,7)
p.add("A6",8,9)
p.show()

canBeDone(p)
