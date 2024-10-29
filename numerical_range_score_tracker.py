# Establish ranges within which the inputs are to be recorded
# Prompt the user to input a number from 1-50. Edit: issue a warning in the occurence of an invalid input and its consequences
# Track the given inputs. Numbers that belong to their respective ranges should be accounted for. Add one score to the range if the input belongs to that range
# In the occurrence of an invalid input, the program will end requesting for user input and will proceed to display the ranges along their recorded scores
# Throughout the program, try to incorporate different methods of tracking the numbers and scores



score_tracker1 = 0
score_tracker2 = 0
score_tracker3 = []
score_tracker4 = []
score_tracker5 = 0
print("Please take note that in the occurence of an invalid input, the program will proceed to display the ranges")
while True:
    user_input = int(input("Please enter a number from 1-50, inclusive: "))
    if 1<= user_input <= 10:
        score_tracker1 += 1
    elif 11<= user_input <= 20:
        score_tracker2 += 1
    elif 21<= user_input <= 30:
        score_tracker3.append(user_input)
    elif 31<= user_input <= 40:
        score_tracker4.append(user_input)
    elif 41<= user_input <= 50:
        score_tracker5 += 1
    else:
        break 

num_score_tracker3 = len(score_tracker3)
num_score_tracker4 = len(score_tracker4)
print(f"1 - 10 = {score_tracker1} ")
print(f"11 - 20 = {score_tracker2} ")
print(f"21 - 30 = {num_score_tracker3} ")
print(f"31 - 40 = {num_score_tracker4} ")
print(f"41 - 50 = {score_tracker5} ")


