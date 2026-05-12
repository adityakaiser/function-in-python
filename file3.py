
def add(P, Q):
    return P + Q


def subtract(P, Q):
    return P - Q


def multiply(P, Q):
    return P * Q


def divide(P, Q):
    return P / Q


print("Choose an operation:")
print("a) Add")
print("b) Subtract")
print("c) Multiply")
print("d) Divide")


choice = input("Enter your choice (a/b/c/d): ")


num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))


if choice == 'a':
    print("Result:", add(num_1, num_2))

elif choice == 'b':
    print("Result:", subtract(num_1, num_2))

elif choice == 'c':
    print("Result:", multiply(num_1, num_2))

elif choice == 'd':
    print("Result:", divide(num_1, num_2))
   

else:
    print("Invalid input! Please enter a, b, c, or d.")
