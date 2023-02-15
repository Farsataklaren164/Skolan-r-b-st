import math

print("Bråk ett")
matte1 = int(input("skriv en täljare:"))
matte2 = int(input("skriv en nämnare:"))

print("Bråk två")
matte3 = int(input("skriv en täljare:"))
matte4 = int(input("skriv en nämnare:"))

print("Bråk tre")
matte5 = int(input("skriv en täljare:"))
matte6 = int(input("skriv en nämnare:"))

SummaTaljare = (matte1*matte4*matte6)+(matte3*matte2*matte6)+(matte5*matte2*matte4)
SummaNamnare = matte2*matte4*matte6

gcd = math.gcd(SummaTaljare, SummaNamnare)
print(SummaTaljare/gcd, "\n" "---" "\n", SummaNamnare/gcd)