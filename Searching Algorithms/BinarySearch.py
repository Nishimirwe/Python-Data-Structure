#This function check if middle element is one we want. If yes it returns middle index
#if not, it does the same on two array sides recursively
#After all steps, if value is not found, -1 is returned

def BinarySearch(arr,start,end,value):
    mid=int((start+end)/2)
    if arr[mid]==value:
        return mid
    elif end==start:
        return -1
    else:
        if arr[mid]<value:
            return BinarySearch(arr,mid+1,end,value)
        else:
            return BinarySearch(arr,start,mid-1,value)

def BinarySearchLoop(arr,start,end,value):
    while 1:
        mid=(start+end)//2
        if value==arr[mid]:
            return mid
        elif end==start:
            return -1
        elif value>arr[mid]:
            start=mid+1
        else:
            end=mid-1

li=[1,2,3,4,5,6,7,8,9]
print(BinarySearchLoop(li,0,len(li)-1,9))
print(BinarySearch(li,0,len(li)-1,6))
