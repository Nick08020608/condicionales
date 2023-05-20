#Design an algorithm that reads the student's name and reads if he/she is an add-on to the University and applies a discount to him/her.

student_name= input("Please enter your name: ")
enrollment_value = int(input("Please enter the tuition fee: "))
message = input("You are a university attaché (Yes or No): ")
discount = enrollment_value*0.30
Value_to_be_paid = enrollment_value-discount

if message == "Yes":
    print(f"because you have a 30% discount for being a member of the university, the registration fee will be of {Value_to_be_paid:.0f}")
else:
    print("As you are not added by the university then your tuition value will remain the same.")
