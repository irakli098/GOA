name = "irakli" 
# name არის ცვლადი 
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# ="irakli" არის ცვლადისთვის მიშვნელობა 

surname = "somkhishvili" 

print(name) 
# print ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი 
# name = "irakli" ეს არის str(stirng) ტიპის ცვლადი 
# სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები 

age = 21 # ეს არის int(integer) ტიპის ცვლადი (მთელი რიცხი) 
height = 1.78 # ეს არის float ტიპის ცვლადი (ათწილადი)
 
knows_programming = True # true of false boolean ტიპის ცვლადი 

print(name + " " + surname +" "+ str(age) + " " + str(knows_programming) )
# print(type(age))- age გადაეცა type ფუნქციას 
#,რომელმაც დააბრუნა მისი ტიპი და დაბრუნებული ნებისმიერი სიმბოლო დავპრინტეტ,რომელმაც გაგვაგებინა რომ 
#print(type(age))-ის ტიპი არის int(integer) (მთელი რიცხვი)


print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))