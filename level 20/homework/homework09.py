numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even = even + num
    else:
        odd = odd + num
total = even + odd 
print(total)

print(even)
print(odd)
 