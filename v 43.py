#uppgift 1
n = 2
while n <= 20:
    print(n)
    n += 2
#uppgift 2
summa = 0
while summa < 100:
    n = int(input("Skriv ett nummer Tack: "))
    summa += n
    print("summan är " + str(summa))
#uppgift 3
guess = (" ")
n = "nej"
while guess != n:
    print("Skulle du vilja spela")
    guess = input("Svar: ")
print("Jag vill faktist inte spela med dig heller")
#uppgift 4

import random
secret_num = random.randint(1,100)
guess_count = 0
guess_limit = 10
out_of_guesses = False
print("\n" + "Högre eller lägre spel!")
print("\n" + "Du Har " + str(guess_limit) + "Försök")
int(guess_limit)
while guess != secret_num and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("\n Svar "))
        guess_count += 1
    else:
        out_of_guesses = True
    if secret_num > guess:
        print("Högre")
    elif secret_num < guess:
        print("Lägre")
if out_of_guesses:
    print("\nDu Förlora")
else:
    print("\nDu Vann")
print("Du Gissade " + str(guess_count) + " Gånger")