# 1.Functions are oen used to validate input. Write a function that accepts a single
# integer as a parameter and returns True if the integer is in the range 0 to 100
# (inclusive), or False otherwise. Write a short program to test the function.
 
def validate_input(num):
 if 0 <= num <= 100:
  return True
 else:
   return False
# Test the function
num= int(input("Enter a number :"))
print(validate_input(num))



