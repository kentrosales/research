# convert fahreinheit to celsius
# show extreme, hot, other weather conditions/descriptions
# normal body temp in humans = 98.6

temp_fahreinheit = float(input("Enter Temperature (Fahreinheit):"))
temp_celsius = (temp_fahreinheit - 32) * 5/9

if temp_celsius >= 100:
    print(f"The temperature is {temp_celsius}. You're at the boiling point.")
elif temp_celsius >= 80:
    print(f"The temperature is {temp_celsius}.The weather's too hot.")
elif temp_celsius >= 50:
    print(f"The temperature is {temp_celsius}. It's warm to go outside. Have fun.")
elif temp_celsius >= 24:
    print(f"The temperature is {temp_celsius}. The weather is cool.")
elif temp_celsius >= 0:
    print(f"The temperature is {temp_celsius}. The weather is cold.")
else:
    print(f"The temperature is {temp_celsius}.It's freezing.")