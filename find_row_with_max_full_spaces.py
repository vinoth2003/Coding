def find_row_with_max_full_spaces(R,C,elements):
    matrix=[]
    index=0
    for i in range(R):
        row=elements[index:index + C]
        matrix.append(row)
        index+=C

    space_full=0
    row_index=-1

    for i in range(R):
        full_max_space=matrix[i].count(1)
        if full_max_space > space_full:
            space_full = full_max_space
            row_index = i


    return row_index + 1


R=int(input().strip())  
C=int(input().strip())
elements=[]
for i in range(R*C):
    demo=(int(input().strip()))
    elements.append(demo)

result=find_row_with_max_full_spaces(C,R,elements)

print(result)

