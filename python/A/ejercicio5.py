#A man wants to know how much money is generated by interest in relation to the amount he has invested in the bank He will decide to reinvest the interest as long as it does not exceed $7000, and in that case he designs an algorithm to know how much money he will eventually have in his account. will eventually have in his account.

investment= int(input("Enter the value of the investment: "))
interests= float(input("Enter the required interest value:"))
interest_per_year= investment*interests

if investment <=7000:
    final_salary= investment+interest_per_year
    print("He invests")
else:
    print("does not realize the investment.")