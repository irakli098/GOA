num1 = int(input("enter first number: "))
num2 = str(input("enter second number: "))
num3 = float(input("enter third number: "))
num4 = int(input("enter fourth number: "))
num5 = float(input("enter fifth number: "))

#მთელ რიცხვს და ათწილადს შორის სრულდება მოქმედება ამიტომ ტერმინალში მივიღებთ შედეგს.
print(int(num1) + float(num3))
#მთელ რიცხვებს შორის სრუდება მოქმედება ამიტომ შედეგს მივიღებთ ტერმინალში.
print(int(num1) - int(num4))
# სტრინგი და მთელ რიცხვს შორის სრულდება მოქმედება ამიტომ შედეგს მივიღებთ ტერმინალში.
print(str(num2) * int(num1))
#სტრინგ და ათწილადს შორის მოქმედება არ სრულდება
print(str(num2) / float(num3))
#ათწილადებს შორის სრულდება მოქმედება ამიტომ შედეგს მივიღებთ ტერმინალში 
print(float(num5) % float(num3))
#ათწილადს და მთელ რიცხვს შორის სრულდება მოქმედება ამიტომ შედეგს მივიღებთ ტერმინალში
print(float(num3) // int(num4))