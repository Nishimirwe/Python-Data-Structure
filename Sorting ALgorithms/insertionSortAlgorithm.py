#In insertiokn sorting algorithm, we move through out an array
#put it in its appropriate place.
# Time complexity O(n2)
#Space complexity O(1)
def insertion(li):
    for j in range(len(li)):
        t=j-1
        k=j
        while li[k]<li[t] and k>0:
            li[k],li[t]=(li[t],li[k])
            k-=1
            t-=1
    return li

arr=[5,3,4,7,2,8,6,9,1]
print(insertion(arr))
