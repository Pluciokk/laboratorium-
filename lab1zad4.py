price = 6.5
km = float(input("Podaj dlugosc drogi (w km) : "))
fuel = float(input("Podaj srednie spalanie w litrach na 100 km : "))
fuelusage = fuel*km/100
print("Zuzycie paliwa wynosi :",round(fuelusage,2))
print("Koszt wynosi",round(fuelusage*price,2))