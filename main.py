import math


a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))
c = int(input("Enter the c value: "))
discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
  print("Number of roots: 0 ")
elif discriminant == 0:
  root = (-b + math.sqrt(discriminant)) / (2 * a)
  print("Number of roots: 1 Root: %f " % (root))
elif discriminant > 0:
  root1 = (-b + math.sqrt(discriminant)) / (2 * a)
  root2 = (-b - math.sqrt(discriminant)) / (2 * a)
  print("Number of roots: 2 \n Roots: %f, %f" % (root1, root2))