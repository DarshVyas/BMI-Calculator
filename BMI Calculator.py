# BMI_CALC

height = float(input("HEIGHT (CMs): "))
weight = float(input("WEIGHT (KGs): "))
int_bmi = (float(weight/height/height)*10000)
bmi = float("{:.2f}".format(int_bmi))
print("Your BMI is =", bmi)
if bmi >= 30.00:
    print('''
You are Obese, Stop eating junk food and start doing exercise!''')
elif bmi >= 25.00:
    print('''
You are Overweight, Attention! you may become Obese soon.''')
elif bmi >= 18.50:
    print('''
Congrats! You have a Normal weight.''')
elif bmi <= 18.50:
    print('''
You are Underweight!''')