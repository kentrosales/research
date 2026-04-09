attempts = 3
saved_PIN = "1234"
balance = 500

print("Hello, Welcome to the World Bank.")

while attempts > 0:
    PIN = input("Please Enter Your 4-Digit PIN:")
    if PIN == saved_PIN:
        withdraw_amount = int(input("PIN verification successful! Please enter withdrawal amount:"))
        if withdraw_amount % 10 != 0 :
            print("You can only withdraw to multiples of 10. Please try again.")
        elif withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw_amount
            print(f"Withdrawal Successful. Your balance is now {balance}")
        exit
    else:
        attempts -= 1
        print("Please enter PIN again.")
if attempts == 0:
    print("Your account has been locked.")



