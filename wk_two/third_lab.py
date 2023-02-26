# if

# x = 9

# if x > 5:
#     x += 1
#     print(x)
# print("done")

# if True:
#     print("hi")



# name = "Foster"
# if name == "Nana":
#     print("You're the professor.")

# print("Okay")


# # if/else

# answer = int(input("What is 4 * 6: "))

# if answer == 24:
#     print("Correct")
#     print("You are intelligent")
# else:
#     print("Ooo Noo.")
#     print("You need to learn hard")

# answer2 = input("Are an African or European? ")

# if answer2 == "African":
#     print("Black is king")
# else:
#     print("You are have to visit Africa")

# print("We are the Best content in the world")

# Basketball

# points = int(input("What is the score line of your team: "))
# points = points - 3

# lead = input("Who has the ball? The leading team or the other team? ")

# if lead == "other team":
#     points -= 0.5
# if lead == "leading team":
#     points += 0.5

# if points < 0:
#     points = 0

# seconds = int(input("How many seconds are left in the game? "))

# if points > seconds:
#     print("SAFE")
# else:
#     print("NOT SAFE")


age = int(input("What is your age?: "))

if age >= 18:
    print("You are eligible to vote")
elif  age > 0 and age < 18:
    print("You don't have the right to vote")
elif age > 150:
    print("I think you are a Ghost")
else:
    print("You are not yet born")