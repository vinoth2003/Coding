def total_sum(n):
    return sum(int(digit) for digit in str(n))

def repeted_sum(N,R):
    if R==0:
        return 0
    first_input=total_sum(N)
    result=first_input*R

    while result>=10:
        result=total_sum(result)

    return result




N=input().strip()
R=int(input().strip())

output = repeted_sum(N,R)
print(output)