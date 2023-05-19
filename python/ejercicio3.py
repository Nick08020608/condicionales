#Design an algorithm that stores the trainee's name, course name, final grade, the number of classes in the semester and the number of failures. In case the failures exceed 30% of the number of classes, the failed grade should be displayed and a zero (0) grade will be given.

name_of_trainee= input("Enter the trainee's name:")
curse_name= input("Enter the name of the course: ")
number_of_classes= int(input("Enter the total classes for the semester: "))
number_of_faults= int(input("Enter the number of classes missed: "))
percentage_of_faults = number_of_classes*0.30

if number_of_classes <= percentage_of_faults:
    print("I approve the subject.")
else:
    print("I fail the class.")
