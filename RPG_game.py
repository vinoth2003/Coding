def monster_defeat(n,e,power,bonus):
    monsters=list(zip(power,bonus))

    monsters.sort()
    count = 0

    for power,bonus in monsters:
        if(e>=power):
            e+=bonus
            count+=1
        else:
            break
    return count
n=int(input("Num of monster:"))
e=int(input("Experience level:"))
power=[78,130]
bonus=[10,0]

print (monster_defeat(n,e,power,bonus))

# def max_monsters_defeated(n, e, powers, bonuses):
#     # Combine powers and bonuses into a list of tuples
#     monsters = list(zip(powers, bonuses))
    
#     # Sort monsters based on their power requirements
#     monsters.sort()
    
#     count = 0  # Initialize the count of defeated monsters
    
#     # Iterate through the sorted list of monsters
#     for power, bonus in monsters:
#         if e >= power:  # Check if current experience is enough to defeat the monster
#             e += bonus  # Increase experience by the monster's bonus
#             count += 1  # Increase the count of defeated monsters
#         else:
#             break  # Stop if the monster cannot be defeated
    
#     return count  # Return the total number of defeated monsters

# # Input from user
# n = int(input("Enter the number of monsters: "))
# e = int(input("Enter the initial experience: "))

# powers = []
# bonuses = []

# print("Enter the power required for each monster:")
# for _ in range(n):
#     power = int(input())
#     powers.append(power)

# print("Enter the bonus for defeating each monster:")
# for _ in range(n):
#     bonus = int(input())
#     bonuses.append(bonus)

# # Calculate the maximum number of monsters that can be defeated
# result = max_monsters_defeated(n, e, powers, bonuses)

# # Output the result
# print("Maximum number of monsters defeated:", result)

