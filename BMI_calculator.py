#bmi calculator

height =float(input("enter your height in m: "))
weight= float(input("enter your weight in kg: "))
bmi=weight/height**2
bmi_as_int=int(bmi)
print(bmi_as_int)