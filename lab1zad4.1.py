import random
price = 6.5
km = random.randint(1, 100000)
print("Wylosowana droga wynosi : ",km)
fuel = float(input("Podaj srednie spalanie w litrach na 100 km : "))
fuelusage = fuel*km/100
print("Zuzycie paliwa wynosi :",round(fuelusage,2))
print("Koszt wynosi",round(fuelusage*price,2))