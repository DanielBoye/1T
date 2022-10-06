import math

radius = int(input("Hva er radiusen? "))
pi = (math.pi)

utregning = 4*pi*radius**3

svar = utregning/3

print(f"Volumet blir {round(svar, 2)} cm.") 
