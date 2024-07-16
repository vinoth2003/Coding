def maximum_guest(T,E,L):
    current_guest=0
    max_guest=0

    for i in range(T):
        current_guest+=E[i]-L[i]
        if current_guest>max_guest:
            max_guest=current_guest

    return max_guest


T=int(input().strip())
E=list(map(int,input().strip().split()))
L=list(map(int,input().strip().split()))


result=maximum_guest(T,E,L)
print(result)