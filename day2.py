# Day 2 – Python Basics

# 🔹 Integers
chetan = 100
print(chetan / 1)   # Output: 100.0

# 🔹 Strings
yashu = "chetan"
print(yashu * 5)    # Output: chetanchetanchetanchetanchetan

# 🔹 Booleans
chetan = True
sreeja = False
joshika = False
print(joshika and sreeja)  # Output: False

# 🔹 Type Conversion
a = 10
b = str(a)
print(b)            # Output: "10"

# ❌ Error Example
# Strings with non-numeric characters cannot be converted to float/int
c = "10S"
# d = float(c)      # This will raise ValueError
# print(d)

# Extra integer example
abc = 100
print(abc)          # Output: 100


# PROGRAM 1 — Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)


# PROGRAM 2 — Simple Bill Calculator
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print("Total bill:", total)


# PROGRAM 3 — Temperature Converter (Celsius → Fahrenheit)
# Formula: F = (C × 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
