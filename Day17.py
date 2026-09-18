#day 17 of learning python --- Function with default parameter
#A default argument is a parameter that already has a value.
def greet(name="Guest"):
    print("Hello", name) 
    #name="Guest" is default parameter, 
greet()    # if no value is passed, it will take "Guest" as default value
greet("Alice")  # if a value is passed, it will use that value

'''
Default value = Guest
But user gives = Alice
Therefore Python uses = Alice
'''

#Example 1: Default Age
def student(name, age=18):
    print("Name:", name)
    print("Age:", age)

student("Chetan")

#Multiple Default Arguments
def profile(name="Guest", branch="AIML"):
    print("Name:", name)
    print("Branch:", branch)

profile()

"""
    def student(name, age=18):
    print(name, age) #correct

    def student(name="Guest", age):
    print(name, age) #incorrect, default parameter should be at the end

    ***Normal parameters first***
    ***Default parameters after***

    """


#Example program - Customer Bill Calculation
def calculate_bill(customer_name, bill_amount, discount=0, tax=18):
  print("Customer Name:", customer_name)
  print("Bill Amount:", bill_amount)
  print("Discount:", discount)
  tax_amount = bill_amount * tax / 100
  print("Tax:", tax)
  final_amount = bill_amount - discount + tax_amount
  print("Final Amount:", final_amount)
calculate_bill("Chetan", 1500,10)


#using loops and asking how many customers to calculate bill for
def calculate_bill(customer_name, bill_amount, discount=0, tax=18):
    tax_amount = bill_amount * tax / 100
    final_amount = bill_amount - discount + tax_amount
    return {
        "Customer": customer_name,
        "Bill Amount": bill_amount,
        "Discount": discount,
        "Tax %": tax,
        "Tax Amount": tax_amount,
        "Final Amount": final_amount
    }

# Ask how many customers
num_customers = int(input("How many customers? "))

# Loop through each customer
for i in range(1, num_customers + 1):
    print(f"\nCustomer {i}:")
    name = input("Name: ")
    bill = float(input("Bill Amount: "))
    discount = float(input("Discount (default 0): ") or 0)
    tax = float(input("Tax % (default 18): ") or 18)

    # Call the function
    result = calculate_bill(name, bill, discount, tax)

    # Print neatly
    print("----- BILL SUMMARY -----")
    print("Customer Name:", result["Customer"])
    print("Bill Amount:", result["Bill Amount"])
    print("Discount:", result["Discount"])
    print("Tax %:", result["Tax %"])
    print("Tax Amount:", result["Tax Amount"])
    print("Final Amount:", result["Final Amount"])
    print("------------------------")
