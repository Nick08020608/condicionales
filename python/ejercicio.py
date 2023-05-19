#Diseñe un algoritmo que capture dos números, y que realice la suma de dichos números, y mostrar los datos si es el resultado no es negativo.

number= int(input("Ienter a number: "))
number_two= int(input("enter a number: "))
 
sum= number+number_two

if sum >0:
    print("The value of the sum is: ", sum)
else:
    print("Because it is a negative number I cannot perform the operation....")
