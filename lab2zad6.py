n = int(input("Podaj liczbe studentów : "))

temp = 0

i = 0

while i < n:

    pkt = int(input("Podaj ilość pkt dla studenta w zakresie od 0 do 100 : "))
    if pkt < 0 or pkt > 100:
        print("Wartosc spoza zakresu, podaj poprawna ")
        continue
    temp = temp + pkt
    i += 1
if n <= 0:
    print("Ilosc studentow musi byc wieksza od zera")
else:
    print("Srednia punktow dla",n,"studentów wynosi",temp/n)