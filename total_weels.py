def find_vechile(v,w):
    if w<2 or w%2!=0 or v>=w:
        return "Invalid Input"
    
    TW = (4*v - w)//2
    FW = v-TW


    if TW<0 or FW<0:
        return "Invalid input"
    return f"TW = {TW} FW = {FW}"


v=int(input().strip())
w=int(input().strip())

result=find_vechile(v,w)
print(result)


