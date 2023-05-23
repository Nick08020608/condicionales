#Perform an algorithm where you do the following A number to be stored in a variable called numberDiacomparison of values between 1 and 7 and display the name of the day next to the value.

def week(numberDay):

    if numberDay == 1:
        print("Thi day of the week is Monday")
    elif numberDay == 2:
        print("Thi day of the week is Tuesday")
    elif numberDay == 3:
        print("Thi day of the week is Wednesday")
    elif numberDay == 4:
        print("Thi day of the week is Thursday")
    elif numberDay == 5:
        print("This day of the week is Friday")
    elif numberDay == 6:
        print("This day of the week is Saturday")
    elif numberDay == 7:
        print("This day of the week is Sunday")
    else:
        print("This day of the week does not exited")

week(input("Write the day you want to address (write it from 1 to 7): "))