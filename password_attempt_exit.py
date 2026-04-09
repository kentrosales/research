saved_password = '1234'
attempts = 0
max_attempts = 3

while max_attempts > attempts:
    user_input = (input("Enter Your Password: "))

    if user_input.lower() == 'exit':
        print("Program terminated.")
    
    if user_input == saved_password:
        print("Access granted!")

    else:
        print("Access denied. Remaining attempts: ", max_attempts)
        max_attempts -= 1

if max_attempts == 0:
    print("Your account is locked.")