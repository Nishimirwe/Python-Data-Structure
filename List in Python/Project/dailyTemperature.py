import numpy as np
def temp(li):
	sum=0
	count=0
	for i in li.values():
		sum+=i
		count+=1
	return sum/count

def whatAbove(li):
	names=({})
	for i in li.keys():
		if li.get(i)>temp(li):
			names.update({i:li.get(i)})
	return names
d=input("How many days: ")
d=int(d)
li=({})
for i in range(d):
	t=input("Day "+str(i+1)+"'s name: ")
	t1=input("Day "+str(i+1)+"'s temperature ")
	t1=int(t1)
	li.update({t:t1})
print("Average is ",temp(li))
print("Days above average are ",len(whatAbove(li))," and are: ",end=' ')
for i in whatAbove(li).keys():
	print(i,"=>",whatAbove(li).get(i),", " ,end=' ')
print()

