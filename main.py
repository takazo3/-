import random
# Split string method
names_string = input("ローマ字でカンマで区切って全員の名前を入力して！")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# num_items = len(names)

# choice = random.randint(0, num_items -1)
# person_who_will_pay = names[choice]

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " さんゴチになります!")
