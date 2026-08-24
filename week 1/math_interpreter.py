x = float(input("enter x: "))
y = input("enter y(+, -, /, *): ")
z = float(input("enter z: "))

if y == "+":
    print(float(f"{x +  z:.1f}"))
elif y == "-":
   print(float(f"{x -  z:.1f}"))
elif y == "/":
    print(float(f"{x /  z:.1f}"))
elif y == "*":
  print(float(f"{x *  z:.1f}"))
