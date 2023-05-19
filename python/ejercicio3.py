#Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso, nota definitiva, el numero de clases en el semestre y el número de las fallas. En el caso de que las fallas superen el 30% del número de clases se debe mostrar la nota que no aprobó y se calificara cero(0)

name_of_trainee= input("Enter the trainee's name:")
curse_name= input("Enter the name of the course: ")
number_of_classes= int(input("Enter the total classes for the semester: "))
number_of_faults= int(input("Enter the number of classes missed: "))
percentage_of_faults = number_of_classes*0.30

if number_of_classes <= percentage_of_faults:
    print("I approve the subject.")
else:
    print("I fail the class.")
