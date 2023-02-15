#uppguft 1
user_input = input("skriv ett ord: ")
for letter in user_input:
    print(letter)
#uppgift 2
n1 = int(input("skriv ett nummer"))
for i in range(n1):
    print("|" + i * " " + " \\")
#uppgift 3
n2 = int(input("skriv ett till nummer: "))
print(" " + n2 * "_")
for n in range(n2):
    print("|" + n2 * " " + "|")
print(" " + n2 * "-")
#4
n = 0
n4 = int(input("skriv ett till nummer"))
for i in range(0, n4+1):
    n = n + i
print(n)