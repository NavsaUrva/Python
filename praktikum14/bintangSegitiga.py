print ("======= PROGRAM BINTANG-BINTANG SEGITIGA =======")
print ("================================================")

a = 7
for i in range (0, a):
    for j in range (0, i):
        print("*", end="")
    print("")

for i in range (0, a):
    for j in range (0, a):
        print("*", end="")
    a-=1
    print("")