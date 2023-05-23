#The sofia store validates the value of the purchase if the value of the purchase is more than than 40 thousand.

print("Welcome to the sofia store")

def store (Value_one):
    
    if Value_one >= 40000:
        color_of_the_ballot= input("\nChoose the type of ballot these are all the colors that there are so far:\n red, white, black, yellow and green: ")
        if color_of_the_ballot == "red":
            the_ballot_red= Value_one*0.10
            result=Value_one-the_ballot_red
            print(f"Tthe value of the ballot is {Value_one} but it has a 10% discount so the final value is {result} ")
        elif color_of_the_ballot == "white":
            the_ballot_white= Value_one*0.15
            result= Value_one-the_ballot_white
            print(f"The value of the ballot is {Value_one} but it has a 15% discount so the value is {result}")
        elif color_of_the_ballot == "black":
            the_ballot_black= Value_one*0.20
            result= Value_one-the_ballot_black
            print(f"The value of the ballot is {Value_one} but is has a 20% discount so the value is {result}")
        elif color_of_the_ballot == "yellow":
            the_ballot_yellow= Value_one*0.20
            result= Value_one-the_ballot_yellow
            print(f"The value of the ballot is {Value_one} but is has a 20% discount so the value is {result}")
        elif color_of_the_ballot == "green":
            the_ballot_green= Value_one*0.30
            result= Value_one-the_ballot_green
            print(f"The value of the ballot is {Value_one} but is has a 30% discount so the value is {result}")
    else:
        print("As the price is less than 40 thousand, no discount is applied to the ballot.")
store(Value_one=int(input("Insert un value of tht product: ")))
