def message(name):
     print("What's up fam?")

name=str(input("Enter the name: "))

if name=="monkey":
     raise Exception("I hate you")
else:
     message(name)
