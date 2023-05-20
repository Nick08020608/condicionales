

side_of_square = int(input("enter the value of the side of the square: "))

area_of_the_square= side_of_square**2

if side_of_square > 10:
    print(f"The area of the square is {area_of_the_square}. The opertion is: {side_of_square}**2 and the result is {area_of_the_square}")
else:
    print(f"Not applicable. The value of the side of the square must be greater than 10 and the value given is: {side_of_square}")