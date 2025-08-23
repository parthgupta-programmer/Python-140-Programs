# Program 27
# Write a Python Program to calculate the BMI(Body Mass Index).

class NonNegativeError(Exception):
    pass
try:
    weight=float(input("Enter your weight in kg:"))
    height=float(input("Enter your height in meters:"))

    if (weight<0 or height<0):
        raise NonNegativeError("Height and Weight cannot be negative.Kindlu enter positive values.")
    bmi=weight/(height*height)
    print("Your BMI is : ",(weight/(height*height)))
    if(bmi<=18.5):
        print("You are Underweight!!")
    elif(18.5 < bmi <=24.9):
        print("You weight is Normal... Congratulations!!")
    elif(24.9 < bmi <= 29.29):
        print("You are Overweight!!")
except ValueError:
    print("Wrong Input!!")
except ZeroDivisionError:
    print("Height cannot be zero!!")
except NonNegativeError as alias:
    print(alias)