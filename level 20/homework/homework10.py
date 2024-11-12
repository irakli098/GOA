numbers = [-3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
positive = 0
negative = 0
for num in numbers:
    if num > 0:
        positive = positive + num
    elif num < 0:
        negative = negative + num
total = negative + positive
print(positive)
print(negative)
print(total)

