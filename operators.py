price = 500                                  # actual price for the product
quantity = 4                                 # these are the quantity of products available
discount = 0.1                               # this is ten percent of the rate
total = price * quantity                     # should be 2000
discount_amount = total * discount           # it should be 200 which is 2000 * 0.1
final_amount = (total - discount_amount)     # my guess: 1800.0

print(discount_amount)                         # should be 200
print(final_amount)                            # 1800 because its total(2000) - discount_amount(200)
print(final_amount > 1500)                     # my guess: True
print(total)                                   # should be 2000