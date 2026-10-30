price = float(input("Enter Amount: "))  # this uses float because amount has decimals
quantity = int(input("How many do you want?: ")) # this uses whole numbers which is integer because you cant order or get something as half example you cannot order a book of 1.5
total = price * quantity  # my guess is it will multiply price_text with whatever  the user inputs 
print(total)

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
print(first + second)    # my guess for 5 and 4: 9
print(first - second)    # my guess for 1 and 4: 1
print(first * third)     # my guess for 2 and 3: 6

maths = str(input("What textbook do you want?: "))
quantities = str(input("How many textbooks do you need?: "))
order = f"{maths} {quantities}"
print(order)