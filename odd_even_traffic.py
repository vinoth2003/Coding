def calculte_fine(N,a,D,X):
    check_odd=D%2!=0
    totaltax=0

    for digit in a:
        if check_odd and digit%2==0:
            totaltax+=X
        elif not check_odd and digit%2!=0:
            totaltax+=X

    return totaltax






N=int(input().strip())
a=[int(input().strip()) for _ in range(N)]
D=int(input().strip())
X=int(input().strip())


result=calculte_fine(N,a,D,X)
print(result)

