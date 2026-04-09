import sys
print("Welcome to WhiteCloud Grammar School!")

#AGE
age = int(input("Please enter your age: "))
if age >= 18:
    print("Approved. You are eligible to study. Please proceed to next step.")
elif age >=16:
    international_fee = input("Are you gonna be paying an international fee? yes or no. ").lower()
    if international_fee == 'yes':
        print("International criteria met. Please proceed to next step.")
    else:
        print("Please contact student advisor.")
        sys.exit()
else:
    print("Please contact student advisor.")
    sys.exit()

 #VISA       
print("--STUDENT ELIGIBILITY (RIGHT-TO-STAY STATUS)--")     
visa = input("Do you currently hold a New Zealand Visa?").lower()
if visa == 'yes':
    None
else:
    print("Please contact student advisor.")
    sys.exit()

right_to_stay = input("Does it allow you to live and study in NZ?")
if right_to_stay == 'yes':
    print("Student right-to-stay verified. Please proceed to next step.")
else:
    print("Please contact student advisor.")
    sys.exit()

#DISTANCE FROM SCHOOL
distance_from_school = int(input("How far (in km) do live from the campus?"))
if distance_from_school >= 4:
    print("Student lives >4 km from the campus")
else:
    print("Student lives less than 4km from the campus")

#SUMMARY
enroll_status = [age >=18, age>=16, right_to_stay == 'yes', distance_from_school <= 4]
if enroll_status == [True, True, True, True]:
    print("Student successfully enrolled! Enjoy your journey in WhiteCloud Grammar School!")
else:
    print("Application declined. Please contact student advisor.")

#Assertion
#if enroll status = True:
#   print('This is a positive feedback')
#else:
#   print('This is a negative feedback')

    

   
