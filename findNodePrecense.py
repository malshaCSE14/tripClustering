a= open("adjacencyPairs.txt", "r")
nodelist1 = []
zz = a.read()
zzz = zz.split("\n")
for x in zzz:
    nodelist1.append(x.strip().split(" ")[:2])

b = open("validTrips.txt", "r")
k = b.readline().strip()
r= []
lineNo = 1
while k != "":
    coor = k.split(" ")
    print lineNo
    lineNo+=1
    k = b.readline().strip()
    for i in range(len(coor)-1):
        if ([coor[i], coor[i+1]] not in nodelist1) and ([coor[i+1], coor[i]] not in nodelist1):
            print [coor[i], coor[i+1]]