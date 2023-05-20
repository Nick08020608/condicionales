#Crear un algoritmo que lea el nombre de un empleado, su salario básico por hora, el nro. de horas trabajadas en un mes.

employee_name= input("Enter your name: ")
minimum_salary= 1030000
transportation_subsidy= 70000
salary_hours= int(input("Enter your salary for hours: "))
hours_for_jobs= int(input("Enter your hours for job: "))
salary_monthly= salary_hours*hours_for_jobs
two_minimum_salary= 2*minimum_salary
if salary_monthly >= two_minimum_salary:
    print(f"Employee name: {employee_name}\nSalary minimum for empleyee: {salary_hours:.0f},\nTransportation subsidy: {transportation_subsidy:.0f},\nhours for jobs:  {hours_for_jobs:.0f},\nYour monthly hourly salary is  {salary_monthly:.1f}")
else:
    print(f"Empleyee name: {employee_name},\nSalary minimium for empleyee: {salary_hours:.0f},\nhours for jobs: {hours_for_jobs:0f},\nYour monthly hours salary is {salary_monthly}")
    