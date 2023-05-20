#In a chain store, a promotion is made through which the customer gets a discount depending on a randomly chosen number, if the chosen number is less than 65 the discount is 20% of the total purchase if it is greater than or equal to 65 the discount is 30%.

import random

random_number= random.randint(1,100)
total_purchase= float(input("Enter the total purchase: "))
discont_one= 0.2
discont_two= 0.3
first_discont= total_purchase*discont_one
second_discont = total_purchase*discont_two

if random_number <65:
    print(f"The number chosen is {random_number} and the discont is of {first_discont:.0f}")
else:
    print(f"The number chosen is {random_number} an the discont is of {second_discont:.0f}")
