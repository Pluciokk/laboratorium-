import random
price = 6.5
km = random.randint(1, 100000)
print(f"Wylosowana droga wynosi {km}")
fuel = float(input("Podaj srednie spalanie w litrach na 100 km : "))
fuelUsage = round(fuel*km/100,2)
totalCost = round(fuelUsage*price,2)
print(f"Zuzycie paliwa wynosi {fuelUsage}")
print(f"Koszt wynosi {totalCost}")