#uppgift 1
nummer1 = input("skriv ett nummer")
nummer2 = input("skriv ditt andra nummer")
nummer3 = input("skriv ditt tredje nummer")
#uppgift 2
list1 = (nummer1), (nummer2), (nummer3)

list2 = []
while list1:
    n = list1[0]
    for x in list1:
        if x < n:
            n = x
    list2.append(n)
    list1.remove(n)
print(n)
print(list2)
list2 = [nummer1], [nummer2], [nummer3]

