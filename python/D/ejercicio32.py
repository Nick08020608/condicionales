# The army's onboarding office needs an algorithm that can allow it to can let it know to know if an applicant to join the institution as a soldier is suitable or not in order to be able to to be able to link it. In order for a person to be eligible, he/she must meet the following requirements: 1. requirements:

#a. If he is a woman, her height must be over 1.60 plus and her age must be between 20 and 25 years old. between 20 and 25 years of age.

#b. If the applicant is male, his height must be over 1.65 plus and his age must be between 18 and 24 years of age. his age must be between 18 and 24 years old.

#c. Both women and men must be single.

#Design the algorithm in such a way as to report whether or not an applicant is fit or unfit to enter the army. to join the military.

print("Wellcome to the Army Nacional of the colombian\n")

print("Please enter your name: ")

def Army(genre, age, height, marital_status):

    if genre.upper() == "female" and age >= 20 or 25 and height >= 1.62 and marital_status.upper() == "Soltero":
        print("You are eligible to join the army")
    elif genre.upper() == "male" and age >= 18 or 24 and height >= 1.65 and marital_status.upper() == "Soltero":
        print("You are eligible to join the army")
    else:
        print("You are not eligible to join the army")

Army(input("Please enter your gender: "), int(input("Please enter your age: ")), float(input("Please enter your height: ")), input("Please enter your marital status: "))
