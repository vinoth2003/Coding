def count_greater_element(arr):
    count=1
    greater_now=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>greater_now:
            count+=1
            greater_now=arr[i]
    return count
    



n=int(input())
arr=[]
for i in range(n):
    element=int(input())
    arr.append(element)

result=count_greater_element(arr)
print(result)