weight = int(input())
height = float(input())
bmi = round(float(weight / (height)**2) , 2)
print("{:.2f}".format(bmi))
if bmi<18.5 :
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else :
    print("Obese")
