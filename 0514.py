price = 0
zone = int(input("Enter your number of zones:"))
age = int(input("Enter your age:"))

if zone == 1:
    price = 2.75
elif zone == 2:
    price = 3.25
elif zone == 3:
    price = 4.5
else:
    print("Pls enter a number between 1 and 3")


if age <= 18 or age >= 65:
    price = price * 0.8

print("Your ticket price is:", price)

money = float(input("Enter your money:"))

if money == 2.75:
    print("zone 1 with no discount")
elif money == 3.25:
    print("zone 2 with no discount")
elif money == 4.5:
    print("zone 3 with no discount")
elif money == 2.2:
    print("zone 1 with discount")
elif money == 2.6:
    print("zone 2 with discount")
elif money == 3.6:
    print("zone 3 with discount")