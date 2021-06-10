def gameOfThrones(s):
    # Write your code here
    str=list(s)
    helper=[]
    count=0
    if str==str.sort(reverse=True):
        return "YES"
    else:
        for i in str:
            if str.count(i)%2!=0 and i not in helper:
                count+=1
                helper.append(i)
                if count>1:
                    return "NO"
        return "YES"
print(gameOfThrones("cdcdcdcdeeeef"))
