noise_level = int(input("Please indicate noise level from 40 - 130"))
if noise_level >= 130:
    print("Jackhammer")
elif noise_level >=106:
    print("Lawnmower")
elif noise_level >= 70:
    print("Alarm Clock")
elif noise_level >= 60:
    print("In between Alarm Clock and Quiet Room")
else:
    print("Quiet Room)")
