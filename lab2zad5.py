n = int(input("Podaj liczbe studentów : "))

temp = 0

i = 0

while i < n:
    i += 1
    print("Student nr ",i)
    temp = temp + int(input("Podaj ilość pkt dla studenta  : "))
if n <= 0:
    print("Ilosc studentow musi byc wieksza od zera")
else:
    print("Srednia punktow dla",n,"studentów wynosi",temp/n)

