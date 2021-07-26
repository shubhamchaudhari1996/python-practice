a = float(input("Enter the length of the first side in cm : "))
b = float(input("Enter the length of the second side in cm : "))
c = float(input("Enter the length of the third side in cm : "))

if ((a+b)>c and (b+c)>a and (a+c)>b):
  print("valid input, and perimeter is: ", a+b+c)
else:
  print("invalid input")