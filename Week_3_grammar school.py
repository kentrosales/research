# DISTANCE FROM SCHOOL
distance_from_school = 4
walking_distance = 0


walking_distance = int(input("How far (in km) are you from school? (km): "))
total_walking_distance = distance_from_school - walking_distance
if walking_distance >= distance_from_school:
    print("Student does not live less than 4 km from school")
else:
    print("Student lives less than 4 km from school")

#AGE

age = int(input("Please enter your age: "))
print(f"Age:", (int(age)))
if age >= 18:
    print("Student is not a MINOR")
else:
    print("Student is a MINOR")

right_to_stay = "Yes"

right_to_stay = input("Do you have rights to stay in NZ? Yes or No. :")
if right_to_stay == "Yes":
    print("Student has rights to stay in NZ.")
elif right_to_stay == "yes":
    print("Student has rights to stay in NZ.")
else:
    print("Student does not have the right to stay in NZ.")

enroll = [total_walking_distance >=4, age >= 18]
enroll = input("Enroll student?")
if enroll == 'Yes':
    print("Student has been enrolled")
elif enroll == 'yes':
    print("Student has been enrolled")



