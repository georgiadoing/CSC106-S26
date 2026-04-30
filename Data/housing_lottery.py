# Created by: Evan Peck (Bucknell University)
# - Contact: evan.peck@bucknell.edu
# - Last Modified: September, 2019

# Keeps track of the point total during questions
current_score = 0

# A header to start the program
print("-------------------------------")
print("   HOUSING SCORE CALCULATOR")
print("-------------------------------")
print()

# Assign points based on class year
print("QUESTION 1")
year_ans = input("What year are you? (1, 2, 3, 4): ")

if year_ans == "1":
    current_score += 1
elif year_ans == "2":
    current_score += 2
elif year_ans == "3":
    current_score += 3
elif year_ans == "4":
    current_score += 4

# If the student is >= 23 years old, give them another point
years_old = input("How old are you?: ")

if int(years_old) >= 23:
    current_score += 1

# At the end of the program, tell the user their score
print()
print("------YOUR HOUSING SCORE----------")
print("Your housing points score is", current_score)
print("----------------------------------")