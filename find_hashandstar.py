def find_difference(S):
    star_count=S.count("*")
    hash_count=S.count("#")

    difference = star_count-hash_count

    return difference

S=input()
result=find_difference(S)
print(result)