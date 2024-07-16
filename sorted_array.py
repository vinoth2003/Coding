N=int(input("Enter the number of array:"))
arr=[]
for i in range(N):
    arr.append(int(input()))
for i in sorted(arr):
    print(i,end=" ")
