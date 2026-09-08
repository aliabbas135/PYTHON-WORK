# Python weight converter

weight = float(input("Enter your weight: "))
unit =  input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} is not a valid unit")

print(f"your weight is:{round(weight, 3)} {unit}")
