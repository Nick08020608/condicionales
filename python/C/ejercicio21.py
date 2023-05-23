#The Auteco motorcycle company has a mid-year promotion, which consists of the following. Honda motorcycles have a discount of 4%, Yamaha of 7% and Suzuki of 15%. of 4%, Yamaha 7% and Suzuki 15%, the other brands 3%.

price= int(input("Enter the price of the motocycle: "))
Honda_discount= price*0.04
Yamaha_discount= price*0.07
Suzuki_discount= price*0.15
discount_for_other_marks= price*0.03

def activity (mark):

    if mark == "Honda":
        total_honda = price - Honda_discount
        print(f"The price of the Honda motorcycle is {price} but with the 4% discount it is {total_honda}")
    elif mark == "Yamaha":
        total_yamaha= price - Yamaha_discount
        print(f"The price of the Yamaha motorcycle is {price} but with the 7% discount it is {total_yamaha}. ")
    elif mark == "Suzuki":
        total_suzuki= price - Suzuki_discount
        print(f"The price of the Suzuki motorcycle is {price} but with the 15% discount it is {total_suzuki}.")
    else:
        total_other_marks= price - discount_for_other_marks
        print(f"Since it does not belong to a suzuki, honda or yamaha then the price will be of {total_other_marks} with 3% discount. ")

activity(mark= input("Enter the motocycle brand: "))