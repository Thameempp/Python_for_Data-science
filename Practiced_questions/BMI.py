# user data
weight = int(input("Enter your weigh in kg: "))
height = float(input("Enter your height in meter:  "))

# BMI calculating function 
def bmi_calc():
    return weight/(height)**2

exact_bmi=bmi_calc()
bmi=round(exact_bmi,1)
print(bmi)


# Your health based on BMI

# overall health based on BMI
if bmi < 18.5:
    print("classified in 'under weight'")
    print("Health risk is 'minimal'")
elif bmi > 18.5 and bmi < 24.9 :
    print("classified in 'Normal weight'")
    print("Health risk is 'minimal'")
elif  bmi > 24.9 and bmi < 29.9 :
    print("classified in 'over weight'")
    print("Health risk is 'increased'")
elif bmi > 30 and bmi < 34.9 :
    print("classified in 'over weight'")
    print("Health risk is 'High'")