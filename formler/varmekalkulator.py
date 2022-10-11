import math
import time

A = int(input("\nVil du ha Kelvin, Celsius eller Fahrenheit.\n\nSvar med,\n\nK = 1;\nC = 2\nF = 3:\n\nroot@ubuntu:~$ "))
B = int(input("\nHvilken type vil du at det skal bli,\n\nK = 1\nC = 2\nF = 3\n\nroot@ubuntu:~$ "))
t = 3 

# Kelvin = 1
# Celsius = 2
# Fahrenheit = 3 

if A == 1: 
    K = float(input("\nSkriv inn Kelivn\n\nroot@ubuntu:~$ "))
    if B == 1:
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
        
        print("Du er dum")
    if B == 2: 
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        K = K - 273.15
        print(f"\nDet blir {round(K, 2)} Celsius.")
    if B == 3:
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        K = K - 273.15
        K = 32 + K * 9 / 5
        print(f"\nDet blir {round(K, 2)} Fahrenheit.")
        
        
if A == 2:
    C = float(input("\nSkriv inn Celcius\n\nroot@ubuntu:~$ "))
    if B == 1: 
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        C = C + 273.15
        print(f"\nDet blir {round(C, 2)} Kelvin.")
    if B == 2:
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        print("Du er dum")
    if B == 3:
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
        
        C = (C * 1.8) + 32
        print(f"\nDet blir {round(C, 2)} Fahrenheit.")
        
    
if A == 3:
    F = float(input("\nSkriv inn Fahrenheit\n\nroot@ubuntu:~$ "))
    if B == 1:
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        F = 5 * (F-32)/9 + 273.15
        print(f"\Det blir {round(F, 2)} Kelvin.")
    if B == 2:
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        F = round(A, 2)
        F = (F-32)*5/9
        print(f"\nDet blir {round(F, 2)} Celsius.")
    if B == 3: 
        print("\nKalkulerer resultater.....\n")
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            
        print("Du er dum")    


# f = float(input("Fahrenheit: "))
# f = round(f, 2)
# celsius = (f-32)*5/9

# print(f"Det blir {round(celsius, 2)} C.")
# c = float(input("Celcius: "))
# k = c + 273.15
# print("kelvin:",round(k,2))



