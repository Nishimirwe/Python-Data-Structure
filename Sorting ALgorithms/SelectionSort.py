#selection sort, it require other array
#we search minimum element in an array and take it in another array
# At the end, the second array will be sorted if first is empty

def findMin(li): #My function to find the Minimum element in an array, but I did not use it in this selection sort, I used in-bulit python list
    m=li[0]
    for i in range(1,len(li)):
        if li[i]<m:
            m=li[i]
    return m,"is the minimum"


#my Insertion
def selection(li):
    sorted=[]
    while len(li) >0:
        m=min(li)
        sorted.append(m)
        li.remove(m)
    return sorted

arr=[44,42,4,1,8,9,2,3,6,0,2,5,5,5,7]
print(selection(arr))
