import math
#1
num1 = int(input("skriv ett nummer"))
num2 = float(input("skriv ett nummer"))
#2
print(float(num1))
print(int(num2))
#3
print(math.ceil(19.7))
print(math.floor(19.7))
#ceil avrundar uppåt för att det är ett tak, floor avrundar ner för att det är golv.
#4
num1 = int(num1)
num2 = int(num2)
gcd1 = math.gcd(num1)
gcd2 = math.gcd(num2)
print(gcd1)
print(gcd2)
#5
print("cirkelns_omkrets")
r = 10
pi = 3.14159265358979323846264338327950288419716939937510
cirkelns_omkrets = (r+r)*pi
print(cirkelns_omkrets)