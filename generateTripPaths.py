edgeInfile = open("edgeNumbers.txt", "r")
# tripInfile = open("trips 2.txt", "r")
outfile = open("tripPaths.txt", "w")

edgeDict = {}
line = edgeInfile.readline()
while line!="":
    tripStrings = line.strip().split(" ")
    # edgeDict[int(tripStrings[0])] = map(int, tripStrings[1:])
    edgeDict[tuple(map(int, tripStrings[1:]))] = int(tripStrings[0])
    line = edgeInfile.readline()
    print tripStrings[0]
edgeInfile.close()

def findNode(junction1, junction2):
    return edgeDict[(junction1, junction2)]

# Generate trip =================================
tripsfileopen = open("trips 2.txt", "r")
line = tripsfileopen.readline()
while line!="":
    tripStrings = line.strip().split(",")[1:]
    a = map(int, tripStrings)
    nodeList = []
    for nodeIndex in range(1,len(a)):
        try:
            node = edgeDict[(a[nodeIndex-1],a[nodeIndex])]
        except KeyError:
            node = edgeDict[(a[nodeIndex],a[nodeIndex-1])]
        nodeList.append(str(node))
    print nodeList
    outfile.writelines(" ".join(nodeList)+"\n")
    line = tripsfileopen.readline()
outfile.close()