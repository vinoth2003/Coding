def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    
def seat_arrange(N):
    if N<2:
        return 0
    return 2 * factorial(N-1)
    
N=int(input().strip())

result=seat_arrange(N)
print(result)
