
#  #0-იდან 20-ის ჩათვლით დაპრინტეთ ყველა მთელი რიცხვი
# for i in range(20):
#     print(i)

#   #დაპრინტეთ პირველი 10 ნატურალური რიცხვი 
# for i in range(1,11):
#     print(i)

#     #დაპტინტეთ 0-იდან 100-ის ჩათვლით ლუწი რიცხვები
# for i in range(0,101,2):
#     print(i)

    #Write a program that calculates and prints the sum of numbers from 1 to 10 using a for loop.
# sum = 0 
# for i in range(1,10):
#         sum = sum + i
#         print(sum)
    
#     #Print the squares of numbers from 1 to 15.
# for i in range(1,16):
#     print(i * i)

  #Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop.
# sum_of_squares = 0
# for i in range(1,6):
#     sum_of_squares = sum_of_squares + i**2
#     print(sum_of_squares)00

    #Print numbers divisible by both 3 and 5 from 1 to 100 inclusive.
# for numbers in range(1,101):
#         if numbers % 3 == 0 and numbers % 5 == 0:
#          print(numbers) 

#Write a program that prints numbers from 10 to 1 in reverse order using a for loop
# for number in range(11,0,-1):
#     print(number)

#შემოატანინეთ მომხმარებელს რიცხვი და დაადგინეთ არის თუ არა დადებითი უარყოფითი ან ნულის ტოლი 
# num = int(input("enter number: "))
# if num > 0:
#     print("დადებითი")
# elif num == 0:
#     print("ტოლია ნულის")
# else:
#     print("ნაკლებია ნულზე")

#შემოატანინეთ მომხმარებელს მისი ასაკი თუ მისი ასაკი 18 წელზე მეტია დაუპრინტეთ “you are adult” თუ 18 წელზე ნაკლები “you are virgin”
# age = int(input("enter your age: "))
# if age > 18:
#     print("you are adult")
# else:
#     age <= 18
#     print("sorry you are not adult")


#დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else 
day = input("enter number: ")
if day == "1": 
    print("1.monday")
elif day == "2":
    print("2.tuesday")
elif day == "3":
    print("3.wednesday")
elif day == "4":
    print("5.thursday")
elif day == "5":
    print("5.friday")
elif day == "6":
    print("6.saturday")
else:
    day == "7"
    print("7.sunday")
