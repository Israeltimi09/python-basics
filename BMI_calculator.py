weight = float(input(Enter your weight in kg:))
height = float(input(Enter your height in m:))
BMI_CAT = weight/height
if BMI_CAT>=40:
    print("Obese class III")
elif BMI_CAT>=35 and BMI_CAT<=39.9:
    print("Obese class II")
elif BMI_CAT>=30 and BMI_CAT<=34.9:
    print("Obese class II") 
elif BMI_CAT>=25.0 and BMI_CAT<=29.9:
    print("Obese class II")    
elif BMI_CAT>=35 and BMI_CAT<=39.9:
    print("Obese class II")