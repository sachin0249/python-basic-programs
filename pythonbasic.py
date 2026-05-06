# Python program for:
# 1. Checking whether a number is Even or Odd
# 2. Swapping two numbers
#    a) Using third variable
#    b) Without using third variable

# -------------------------------
# Even or Odd Program
# -------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# -------------------------------
# Swapping Two Numbers
# -------------------------------

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# a) Using third variable
temp = a
a = b
b = temp

print("\nAfter Swapping using third variable:")
print("a =", a)
print("b =", b)

# Taking input again for second method
a = int(input("\nEnter first number again: "))
b = int(input("Enter second number again: "))

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# b) Without using third variable
a, b = b, a

print("\nAfter Swapping without using third variable:")
print("a =", a)
print("b =", b)
