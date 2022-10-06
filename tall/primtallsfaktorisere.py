print("Primtallfaktorisere 630.")

tall = 630

for faktor in range(2, 630):
    while (tall % faktor == 0):
        print("630 har faktoren:", faktor)
        tall = tall / faktor