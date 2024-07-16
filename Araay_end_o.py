def find_empty_pocket(arr):
    nonzero=[]
    zero_count=0

    for i in arr:
        if (i!=0):
            nonzero.append(i)
        else:
            zero_count+=1

    nonzero.extend([0]*zero_count)

    return nonzero

N=int(input("Enter the number:"))

arr=[]

print("Enter number of array:")

for _ in range(N):
    input_element=int(input())
    arr.append(input_element)

result = find_empty_pocket(arr)

print(" ".join(map(str,result)))
