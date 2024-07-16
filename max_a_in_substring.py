def count_max_a(s,L):
    max_a=0

    for i in range(0,len(s),L):
        substring = s[i:i+L]
        count_a=substring.count('a')
        if count_a>max_a:
            max_a=count_a

    return max_a

s=input().strip()
L=int(input().strip())
result=count_max_a(s,L)
print(result)
