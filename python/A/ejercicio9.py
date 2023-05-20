#Determine if a trainee passes or fails a training and takes his or her average.

first_qualification= int(input("Enter the rating: "))
second_qualification= float(input("Enter the rating: "))
third_qualification= float(input("Enter the rating: "))
average= first_qualification+second_qualification+third_qualification/3

if average >=10:
    print("Approved")
else:
    print("Failed")
    