#A worker needs to calculate his weekly salary, which is obtained as follows: if he works 20 hours or less he is paid $10,000 per hour; if he works more than 20 hours he is paid $35,000 per hour.

works_hours= int(input("Enter your wors hours: "))
weekly_wage_one= works_hours*10000
weekly_wage_two= works_hours*35000


if works_hours <=20:
    print(f"You worked for {works_hours:.0f} hours, then your salary is {weekly_wage_one}.")
else:
    print(f"Your workend for {works_hours:.0f} hours, then your salary is {weekly_wage_two}.")