def square(num):
    print( num**2)
def cube(num):
    print(num**3)


user=input("Enter your choice: ")

choice = {
    "1": square,
    "2":cube
}
num =int(input("enter the number you want to square/cube:"))

try:
    choice[user](num)

except ValueError:
    print("No valid integer")

else:
    print("Your input was recorded successfully.")