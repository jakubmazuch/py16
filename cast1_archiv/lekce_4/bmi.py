vaha = int(input("Zadej váhu v kg: "))
vyska_cm = int(input("Zadej výšku v cm: "))
vyska_m = vyska_cm/100

bmi = vaha/(vyska_m**2)

if bmi < 18.5:
    print(f"BMI: {bmi} - podváha")
elif bmi < 25:
    print(f"BMI: {bmi} - ideální váha")
elif bmi < 30:
    print(f"BMI: {bmi} - nadváha")
elif bmi < 35:
    print(f"BMI: {bmi} - mírná obezita")
elif bmi < 40:
    print(f"BMI: {bmi} - střední obezita")
else:
    print(f"BMI: {bmi} - morbidní obezita")
