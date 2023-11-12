x = int(input("Jaką operacje chcesz wykonać? 1)Dodawanie, 2)odejmowanie, 3)mnozenie, 4)dzielenie, 5)potegowanie (Wpisz liczbe) : "))

a = int(input("Podaj argument 1: "))
b = int(input("Podaj argument 2: "))

if x == 1:
    print("Wynik wynosi : ",a+b)
elif x == 2:
    print("Wynik wynosi : ",a-b)
elif x == 3:
    print("Wynik wynosi : ",a*b)
elif x == 4:
    print("Wynik wynosi : ",a/b)
elif x == 5:
    print("Wynik wynosi : ",a**b)
else:
    print("Podano zlą liczbe")
