f = open("aFile.txt", "a")
f.write("Lite text här \nlkdjfljhgsljhfa")
f.close()

#open and read the file after the appending:
f = open("aFile.txt", "r")
print(f.read())
