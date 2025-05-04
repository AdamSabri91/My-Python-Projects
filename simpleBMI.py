height = int(input("Enter you height : "))
weight = int(input("Enter you weight : "))
BMI = weight / height**2
if BMI <= 18.5 :
    print("You're underweight")
elif BMI >=18.5 and BMI < 25 :
    print("You're normal")
elif BMI >= 25 and BMI <30 :
    print("You're overweight")
else :
    print("You're Obese")