# შექმენით პროგრამა რომელიც გამოითვლის ჯგუფის საშუალო ასაკს. 
# ასევე გამოითვალეთ ყველაზე ხშირად რომელი ასაკი გვხვდება

age = [15,15,16,16,16,16,16,16,15,17,17,17,17,19,21,21,23,25,25,26,32]

sum = 0

for elements in age:
    sum += elements
    num = sum / len(age)
print(num)

ages = [15,15,16,16,16,16,16,16,15,17,17,17,17,19,21,21,23,25,25,26,32]


first_rank = ages[0]

for element in ages:
    if ages.count(element) > ages.count(first_rank):
       first_rank = element


print(first_rank)