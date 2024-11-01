# Establish ranges within which the inputs are to be recorded
# Prompt the user to input a number from 1-50. Edit: issue a warning in the occurence of an invalid input and its consequences
# Track the given inputs. Numbers that belong to their respective ranges should be accounted for. Add one score to the range if the input belongs to that range
# In the occurrence of an invalid input, the program will end requesting for user input and will proceed to display the ranges along their recorded scores
# Throughout the program, try to incorporate different methods of tracking the numbers and scores
# Edit: Give the user the option to see their inputted values assigned at their respective ranges


# Used to record the scores for its ranges
# Defined lists to avoid errors when the range using .count() is empty
score_list1, score_list2, score_list3 = [], [], []
score_tracker4 = 0
score_tracker5_list = []

# Used to store the inputs for display at the last prompt
input_tracker1, input_tracker2, input_tracker3, input_tracker4 = [], [], [], []

print("Please take note that in the occurrence of an invalid input, the program will proceed to display the ranges")
while True:
    try:
        # Asks the user for a numerical input within 1-50
        user_input = int(input("Please enter a number from 1-50, inclusive: "))
        if 1<= user_input <= 10:
            # Edit: My new concept here is to change each elements in the original list then assign it to new defined list, then use .count() to record the score
            input_tracker1.append(user_input)
            # This comprehension format is sourced from stackoverflow.com and was tailored by me accordingly. Link: https://stackoverflow.com/questions/7126916/perform-a-string-operation-for-every-element-in-a-python-list
            edit_input_tracker1 = ["i" for num1 in input_tracker1]
            score_list1 = edit_input_tracker1
        elif 11<= user_input <= 20:
            input_tracker2.append(user_input)
            # Used "i" for much simpler representation
            edit_input_tracker2 = ["i" for num2 in input_tracker2]
            score_list2 = edit_input_tracker2
        elif 21<= user_input <= 30:
            input_tracker3.append(user_input)
            edit_input_tracker3 = ["i" for num3 in input_tracker3]
            score_list3 = edit_input_tracker3
        elif 31<= user_input <= 40:
            # If the user_input is within this range, the program adds 1 to the score tracker assigned to this range
            score_tracker4 += 1
            input_tracker4.append(user_input) 
        elif 41<= user_input <= 50:
            # If the user input is within range, the program stores it in the assigned list and count its elements using len() at the bottom 
            score_tracker5_list.append(user_input)
        else:
            print("An invalid input has been entered. The number of inputs belonging within each ranges are as follows:")
            break
    except ValueError:
        print("An invalid input has been entered. The number of inputs belonging within each ranges are as follows:")
        break

# the .count() counts how many 'i' where on the score_lists. This is the endgame of my method in range 1-10, 11-20, 21-30
score_tracker1 = score_list1.count("i")
score_tracker2 = score_list2.count("i")
score_tracker3 = score_list3.count("i")
score_tracker5 = len(score_tracker5_list)
print(f"1 - 10 = {score_tracker1}")
print(f"11 - 20 = {score_tracker2}")
print(f"21 - 30 = {score_tracker3}")
print(f"31 - 40 = {score_tracker4}")
print(f"41 - 50 = {score_tracker5}")

# Gives the user the option to see their inputted values
while True:
    user_choice = input("Would you like to see the inputs in the ranges?('yes'/'y' or 'no'/'n'): ").lower()
    if user_choice == 'y' or user_choice == 'yes':
        break
    elif user_choice == 'n' or user_choice == 'no':
        print("Thank you for trying the program. Have a nice day!!!")
        quit()
    else:
        print("Please respond using what's only specified")

print(f"1 - 10: {input_tracker1}")
print(f"11 - 20: {input_tracker2}")
print(f"21 - 30: {input_tracker3}")
print(f"31 - 40: {input_tracker4}")
print(f"41 - 50: {score_tracker5_list}")

