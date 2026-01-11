
digits = [0, 0, 0, 0]
new_digits = [0, 0, 0, 0]

for i in range(4):
  digits[i] = int(input("Please enter a number: "))


# if digits[0] % 3 == 0:
# new_digits[0] = digits[0] 
# elif digits[0] % 3 == 1:
# new_digits[0] = digits[0] - 1
# elif digits[0] % 3 == 2:
# new_digits[0] = digits[0] + 1

# if digits[1] % 3 == 0:
# new_digits[1] = digits[1] 
# elif digits[1] % 3 == 1:
# new_digits[1] = digits[1] - 1
# elif digits[1] % 3 == 2:
# new_digits[1] = digits[1] + 1

# if digits[2] % 3 == 0:
# new_digits[2] = digits[2] 
# elif digits[2] % 3 == 1:
# new_digits[2] = digits[2] - 1
# elif digits[2] % 3 == 2:
# new_digits[2] = digits[2] + 1

# if digits[3] % 3 == 0:
# new_digits[3] = digits[3] 
# elif digits[3] % 3 == 1:
# new_digits[3] = digits[3] - 1
# elif digits[3] % 3 == 2:
# new_digits[3] = digits[3] + 1

for i in range(4): 
  if digits[i] % 3 == 0: 
    new_digits[i] = digits[i] 
  elif digits[i] % 3 == 1: 
    new_digits[i] = digits[i] - 1 
  else: 
    new_digits[i] = digits[i] + 1

print("Original digits:", digits)
print("Multiples of 3:", new_digits)




