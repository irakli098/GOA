# 2)  შექმენით პროგრამა რომელიც დაითვლის სიაში რამდენჯერ მეორდება თქვენი სახელი არ გამოიყენოთ count ფუნქცია 

my_list = ["irakli", "irakli", "lazare", "irakli", "tea"]

my_name = input("enter your name: ")

count = 0

for elements in my_list:
    if elements == my_name:
        count += 1
print(count)