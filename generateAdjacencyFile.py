fo = open("edgeNumbers.txt", "r")
line = fo.read()
data = line.split("\n")
fo.close()
fileAdj = open("Adjacency File 2.txt", "w")
for ALines in data:
    ALineElements = ALines.strip().split(" ")
    print  ALineElements
    Anodes = ALineElements[1:3]
    adjacentList = []
    headItem = ALineElements[0]
    if int(headItem)<=3000:
        for BLines in data:
            BLineElements = BLines.strip().split(" ")
            Bnodes = BLineElements[1:3]
            for node1 in Anodes:
                if node1 in Bnodes:
                    element = BLineElements[0]
                    if element != headItem:
                        if int(element)<=3000:
                            adjacentList.append(element)
    fileAdj.writelines(str(headItem)+" "+str(" ".join(adjacentList))+"\n")
fileAdj.close()
print("Adjacency matrix created...!")
