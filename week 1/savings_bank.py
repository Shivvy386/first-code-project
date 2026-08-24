greeting = input("Enter your greeting:")

if greeting.split()[0].lower() == "hello":
    print("0$")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
