#Write a program that allows you to guess a Marvel character based on 3 questions.

skill_one= input("Can it fly?\nYes/No: ")
skill_two= input("Is human?\nYes/No: ")
skill_three= input("Does it have a mask?\nYes/No: ")

if skill_one.upper()=="Yes" and skill_two=="Yes" and skill_three=="Yes":
    print("The superhero is Iron Man.")
elif skill_one.upper()=="Yes" and skill_two=="Yes" and skill_three=="No":
    print("The superhero is Doctor Strange.")
elif skill_one.upper()=="Yes" and skill_two.upper()=="No" and skill_three.upper()=="No":
    print("The superhero is Thor.")
elif skill_one.upper()=="No" and skill_two.upper()=="Yes" and skill_three.upper()=="Yes":
    print("The superhero is Capitain America.")
elif skill_one.upper()=="No" and skill_two.upper()=="No" and skill_three.upper()=="Yes":
    print("The superhero is ")
elif skill_one.upper()=="No" and skill_two.upper()=="No" and skill_three.upper()=="No":
    print("The superhero is ")
else:
    print("What superhero did you think of?")
