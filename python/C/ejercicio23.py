#A customer goes to buy a motorcycle and notices that if he buys it on Tuesday he gets a 10% discount. Tuesday he gets a 10% discount, then if he buys it on Saturday he gets an 18% discount. a discount of 18% to show how much he will pay in each

price= float(input("Enter the price of motocycle: "))
day= input("Enter the day of the purchase. \n Tuesday(T),Saturday(S) or other day(O): ")

if day=="T" or day=="t":
    discount= price*0.10
    total_discount= price-discount
    print(f"as it is a discount day, the value of your motorcycle will be of  {total_discount}")
elif day=="S" or day=="s":
    discount= price*0.18
    total_discount= price-discount
    print(f"as it is a discount day, the value of your motocycle will be of  {total_discount}")
else:
    print(f"not being a discounted day the value of the same.")

