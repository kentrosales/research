import sys

print("Welcome to WhiteCloud Online Shopping")
    #registration
reg_status = input("Are you currently registered to WhiteCloud Online Shopping?")
if reg_status == 'yes':
    print("User is registered to WhiteCloud Online Shopping")
else:
    print("User not currently registered. Purchase declined.")
    sys.exit()
#item count
total_items = int(input("Please enter total no. of items purchased: "))
if total_items >= 1:
    print("More than one item purchased. Please proceed to payment. ")
else:
    print("Purchase attempt declined. You need more than one item purchased to continue.")
    sys.exit()

purchase_status = [reg_status == 'yes', total_items >= 1]
if purchase_status == True:
    print(f"User currently registered with total item Purchased: ", total_items)
    print("Please proceed to payment.")

#MODE OF PAYMENT
final_amount = 4000 #to be paid
saved_pin = '1234'
payment_method = input("Mode of payment: Please press (1)  for card and (2) for cash: ")
#CARD PAYMENT
if payment_method == '1':
    pin = input("Please enter your PIN. ")
    if pin == saved_pin:
        print("Purchase successful! Thank you for shopping with us! Would you like to print an online receipt?")
    else:
        print("PIN not recognized. Please try again.")
    card_payment = int(input("Please enter total amount purchased: "))
    if card_payment == final_amount:
        print("Transaction successful. Thank you for shopping with us!")
    else:
        print("Insufficient funds.")
#CASH PAYMENT
else:
    cash_payment = int(input("Please enter your cash: "))
    if cash_payment == final_amount:
        print("Transaction successful. Thank you for shopping with us!")
    else:
        print("Insufficient funds.")
    
    

            
