#ვთხოვ მომხმარებელს შემოიტანოს 2 რიცხვი და ვარჩევ რიმელია უფრო დიდი
num = int(input("please enter number: "))
num1 = int(input("please enter number: "))
if (num > num1) :
    print("num > num1")
if (num1 > num) :
    print("num1 > num") 
if (num == num1) :
    print("num = num1")
#ვწერ უმცირესი რიცხვიდან უდიდეს რიცხვამდე ყველა რიცხვს
for i in range(num,num1):
    print(i)
    