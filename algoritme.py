from cmath import sqrt
import math as m
import random as r


sum = 0

n = int(input("Hvor mange linjer vil du ha? "))

for i in range(n):
    ax = r.randint(0, 11)
    ay = r.randint(0, 9)    
    bx = r.randint(0, 11)
    by = r.randint(0, 9)
    
    k1 = abs(ax - bx)
    k2 = abs(ay - by)
    
    tilsammen = m.sqrt(k1**2 + k1**2)
    sum = sum + tilsammen

gjennomsnitt = sum/i

print("Gjennomsnitt: " + str(gjennomsnitt))
