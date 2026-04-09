import sys
correct_password = "python123"
attempts = 3


while attempts > 0:
    password = input("Enter Your Password:")
    if password == correct_password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect! {attempts} attempts left.")

if attempts == 0:
    print("Access denied. Exiting")
    sys.exit(1)
