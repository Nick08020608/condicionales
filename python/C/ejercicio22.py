#A un trabajador le descuentan de su sueldo el 4%, si su sueldo es menor o igual a $1000000, si el sueldo está entre $1000000 y $2000000 el 7%, y por encima de 2000000 el 8% calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo.

Salary= float(input("Enter your salary: "))
first_discount= Salary*0.04
second_discount= Salary*0.07
third_discount= 0.08

if Salary <= 1000000:
    print(f"because your salary is of {Salary} will have a discount of 4 percent of his salary and his salary will be reduced to {first_discount}. ")
elif Salary == 1000000 or 2000000:
    print(f"because your salary is of {Salary} will have a discount of 7 percent of his salary and his salary will be reduced to {second_discount}")
else:
    print(f"because his salary is higher than 2000000 then he will have a salary discount of 8 percent so his actual salary will be {third_discount}")
