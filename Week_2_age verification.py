#Modify the code to check if the age is a neg number and display error
#Classify users as senior citizen (65+)

age = int(input("Enter your Age:"))

if age >= 65:
    print("Hello, you are eligible for our Senior Citizen voting services.")
elif age >= 18:
    print("You are eligible to vote.")
elif age < 0:
    print("Negative age. Please try again.")
elif age <= 0:
    print("Your age cannot be zero. Please try again.")
else:
    print("You are not eligible to vote")
