print("\n")

#FIRST QUESTION
food = ['pizza', 'bread', 'noodle', 'rice']
del food[2]
print(food)

print(f"My favorite foods are {food[0].title()} and {food[2].title()}")

print("\n")

#SECOND QUESTION
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
input3 = int(input("Enter third number: "))

fav_num = [input1, input2, input3]
for num in fav_num:
    print(num, "is my favorite number")

sum = input1 + input2 + input3

if sum > 30:
    print(f"sum of my favorite number is {sum} which is higher than 30")
else:
    print(f"sum of my favorite number is {sum} which is lower than 30")



print("\n")
#THIRD QUESTION
fav_food = {
    "alice": "sushi",
    "bianca": "pizza",
    "kate": "chicken wing"
}

for name, food in fav_food.items():
    print(f"{name.title()}'s favorite food is {food}.")

print("\n")

#FOURTH QUESTION
i = 1
while i <= 3:
    side = int(input("Input the side length: "))
    area = side * side
    print(f"The area of the rectangle number {i} is {area}")
    i += 1

