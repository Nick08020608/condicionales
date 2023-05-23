#Create a menu where the user must select an option from the basic operations.

def cal(Selections_Operations,Number_one,Number_two):
    
    if Selections_Operations == 1:
        result= Number_one+Number_two
        print(f"The result of operation sum is {result}")
    elif Selections_Operations == 2:
        result= Number_one-Number_two
        print(f"The result of operation subtraction is {result}")
    elif Selections_Operations == 3:
        result= Number_one*Number_two
        print(f"The result of operation multiplication is {result}")
    elif Selections_Operations == 4:
        result= Number_one/Number_two
        print(f"The result of operation division is {result}")
    elif Selections_Operations == 5:
        result= Number_one//Number_two
        print(f"The result of operation division entire is {result}")
    elif Selections_Operations == 6:
        result= Number_one%Number_two
        print(f"The result of operation residue is {result}")
    else:
        print("Please select a valid option")

print(f"The basic operations are:\nsum(1)\nsubtract(2)\nmultiplicacion(3)\ndivision(4)\ndivision entire(5)\nresidue(6)")
cal(Selections_Operations=int(input("Select one operation: ")),Number_one=float(input("Number one: ")),Number_two=float(input("Number two: ")))
