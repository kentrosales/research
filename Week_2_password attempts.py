correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input("Enter your password:")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect! {attempts} attempts left.")

if attempts == 0:
    print("Access denied. Please reset your password.")
