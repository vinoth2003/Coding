def find_sunday(start_day,N):
    week={'sun':0,'mon':6,'tue':5,'wed':4,'thu':3,'fri':2,'sat':1}

    start_day_num=week[start_day]
    count_sunday=0
    for i in range(N):
        result=(start_day_num+i)%7
        if result==0:
            count_sunday+=1

    return count_sunday


start_day=input("Enter the start day of week:").strip().lower()
N=int(input("Enter number the days:"))

output=find_sunday(start_day,N)

print(output)