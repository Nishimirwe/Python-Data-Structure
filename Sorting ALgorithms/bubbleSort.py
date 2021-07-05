#This algorithm use loops to sort data, and its time complexity is O(n2)
def sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j]=(li[j],li[i])
    return li

li=[70,10,80,30,20,40,60,50,90]
print(sort(li))
