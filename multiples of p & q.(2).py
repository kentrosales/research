
p = 4
q = 29
#start counter
start_count = 10

print("Answer: ", end="")

# Loop until the value exceeds q
while start_count <= q:
    # Check if the current value is a multiple
    #  of p
    if start_count % p == 0:
        print(start_count, end=", ")
    
    # Increment the counter to move to the next number
    start_count += 1