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


li=[1,2,4,10,15]
print(BinarySearch(li,0,len(li)-1,1765))
