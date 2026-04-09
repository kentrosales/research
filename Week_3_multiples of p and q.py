p = 4
q = 29

multiples = []
for i in range(10, q + 1): #it's like saying a list of (10, 29 (29+1 =30) *dont include 30)
    if i % 4 == 0:
        multiples.append(int(i))
print(multiples)

