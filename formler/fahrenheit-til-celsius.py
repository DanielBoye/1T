import math

f = float(input("Fahrenheit: "))
f = round(f, 2)
celsius = (f-32)*5/9

print(f"Det blir {round(celsius, 2)} C.")
