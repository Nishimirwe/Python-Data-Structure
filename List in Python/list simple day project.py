#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=input("How many days? ")
n=int(n)
li=[]
for i in range(1,n+1):
    t=int(input("Day temperature "))
    assert type(t) is int,'Only integer'
    li.append(t)
def average(arr):
    return sum(arr)/len(arr)
def aboveAverage(li):
    count=0
    for i in li:
        if i>average(li):
            count+=1
    return count
print("Average: ",average(li))
print(aboveAverage(li)," day(s)' above the average")
    


# In[ ]:




