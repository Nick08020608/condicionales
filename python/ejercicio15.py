#Make an algorithm that calculates the total amount to pay for the purchase of shirts. If three or more shirts are purchased, a 15% discount is applied to the total purchase and if less than 3 shirts are purchased, the discount is 5%.

shirt_value= float(input("Enter the shirt value: "))
number_of_shirt= int(input("Enter the number of shirts: "))
total_value= shirt_value*number_of_shirt
total_without_discount= total_value*0.05
discounted_total= total_without_discount*0.15

if number_of_shirt >= 3:
    print(f"The value of the shirts is {total_value:.0f} but with the 15% discount the total value of the shirts is {discounted_total}")
else:
    print(f"The valur of the shirts is {total_value} but with the 5% discount the total value of the shirts is {total_without_discount}")
