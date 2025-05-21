import math

n1 = float(input("enter first number: ")))
n2 = float(input("enter second number: ")))

print("the square root of", n1, "is", math.sqrt(n1))
print("the square root of", n2, "is", math.sqrt(n2))

print("the larger number is: ")

if float(n1) > float(n2):
    print(n1)
elif float(n1) < float(n2):
    print(n2)
else:
    print("there are same")