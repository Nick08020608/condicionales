#Diseñe un algoritmo que capture dos números, y que realice la suma de dichos números, y mostrar los datos si es el resultado no es negativo.

number= int(input("Ingrese un numero: "))
number_two= int(input("Ingrese un numero. "))
 
suma= number+number_two

if suma >0:
    print("El valor de la suma es: ", suma)
else:
    print("Devido a que es un numero negativo no puedo realizar la operacion...")
