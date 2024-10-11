num1 = int(input("enter number: "))
num2 = int(input("enter second number: "))
num3 = (input("choose : + , -, *, /, :"))
if num3 == "+":
    print(str(num1) + "+" + str(num2) + "=" + str(int(num1) + int(num2)))

elif num3 == "-":
    print(str(num1) + "-" + str(num2) + "=" + str(int(num1) - int(num2)))
elif num3 == "*":
      print(str(num1) + "*" + str(num2) + "=" + str(int(num1) * int(num2)))

else:
       print(str(num1) + "/" + str(num2) + "=" + str(int(num1) / int(num2)))