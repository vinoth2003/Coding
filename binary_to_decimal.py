import math
N=int(input())
b=(1<<(int(math.log2(N))+1))-1
dec_after_toggle=b^N
print(dec_after_toggle)