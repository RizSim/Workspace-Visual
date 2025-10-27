f = open("demofile2.txt", "a")
f.write("Altro contenuto!\n")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())