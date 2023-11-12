a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c= temp
if b > c:
    temp = b
    b = c
    c = temp
print(a,b,c)