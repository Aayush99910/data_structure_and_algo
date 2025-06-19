# def tug_of_war_recursive(students, choices, num_chosen):
#     # If there are not enough students left to build a full team,
#     # return an empty list and float('inf').
#     if len(students)//2 - num_chosen > len(students) - len(choices):
#         return [], float('inf')

#     # Base case, if the number of students chosen is equal to the size of a team
#     if num_chosen == len(students)//2:
#         # Fill choices with False until it's the
#         # same length as students
#         while len(choices) < len(students):
#             choices.append(False)
#         # Initialize variables for tracking the teams' strengths as 0
#         team_1_strength = 0
#         team_2_strength = 0
#         # Enumerate and iterate over choices
#         for i, choice in enumerate(choices):
#             # If student was chosen, add to team 1's strength
#             if choice:
#                 team_1_strength += students[i]
#             # Otherwise, add to team 2's
#             else:
#                 team_2_strength += students[i]
#         # Return choices and difference in strengths
#         return choices, abs(team_1_strength - team_2_strength)

#     # Recursive case without the next student
#     choices_without, diff_without = tug_of_war_recursive(students, choices + [False], num_chosen)
#     # Recursive case with the next student
#     choices_with, diff_with = tug_of_war_recursive(students, choices + [True], num_chosen + 1)
    
#     # If difference was lower with than without,
#     # return choices and difference with
#     if diff_with < diff_without:
#         return choices_with, diff_with
#     # Otherwise, return choices and diff without
#     else:
#         return choices_without, diff_without

# def tug_of_war(students):
#     choices = []
#     num_chosen = 0
#     return tug_of_war_recursive(students, choices, num_chosen)


# students = [16, 18, 3, 4, 5, 14, 7, 13, 8, 17, 15, 6, 10]
# choices, min_diff = tug_of_war(students)

# team_1 = []
# team_2 = []
# for i, choice in enumerate(choices):
#     if choice:
#         team_1.append(students[i])
#     else:
#         team_2.append(students[i])

# print("Team 1:", team_1)
# print("Team 2:", team_2)
# print("Difference:", min_diff)


def tug_of_war_recursion(students, choices, num_chosen):
    if len(students)//2 - num_chosen > len(students) - len(choices):
        return [], float("inf")
    
    if num_chosen == len(students)//2:
        # find the smallest one and return that
        # add everything to team 2 
        while len(choices) < len(students):
            choices.append(False)

        team_1_power = 0
        team_2_power = 0 

        for i in range(len(choices)):
            if choices[i]:
                team_1_power += students[i]
            else:
                team_2_power += students[i]
        
        return choices, abs(team_1_power - team_2_power)
    
    choices_without, diff_without = tug_of_war_recursion(students, choices + [False], num_chosen)
    choices_with, diff_with = tug_of_war_recursion(students, choices + [True], num_chosen + 1)

    # get the smallest difference and then add that 
    if diff_without < diff_with:
        return choices_without, diff_without
    else:
        return choices_with, diff_with

def tug_of_war(students):
    choices = []
    num_chosen = 0
    return tug_of_war_recursion(students, choices, num_chosen)


students = [16, 18, 3, 4, 5, 14, 7, 13, 8, 17, 15, 6, 10]
choices, min_diff = tug_of_war(students)

team_1 = []
team_2 = []
print(choices)
for i, choice in enumerate(choices):
    if choice:
        team_1.append(students[i])
    else:
        team_2.append(students[i])

print("Team 1:", team_1)
print("Team 2:", team_2)
print("Difference:", min_diff)