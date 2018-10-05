infile = open("tripPaths.txt", "r")
lineNo= 1
line = infile.readline()
subsetOf = {}
parents = {}
trips = {}

numberOfClusters = 3

while line!="":
    trips[lineNo] = map(int, line.strip().split(" "))
    # print trips[lineNo]
    line = infile.readline()
    subsetOf[lineNo] = []
    parents[lineNo] = []
    lineNo+=1

for index1 in range(1, len(trips)+1):
    mainTrip = " ".join(map(str, trips[index1]))
    for index2 in range(index1+1, len(trips)+1):
        secondaryTrip = " ".join(map(str,trips[index2]))
        if secondaryTrip in mainTrip:
            subsetOf[index1].append(index2)
            parents[index2].append(index1)
            print index2, "is a subset of", index1
        elif mainTrip in secondaryTrip:
            subsetOf[index2].append(index1)
            parents[index1].append(index2)
            print index1, "is a subset of", index2
print "list is child trips"
# print subsetOf

outfile1 = open("subsetResults/subsets.txt", "w")
for key in subsetOf:
    outfile1.writelines(str(key)+" "+ " ".join(map(str,subsetOf[key]))+"\n")
outfile1.close()

print "list is parent trips"
# print parents

outfile2 = open("subsetResults/parents.txt", "w")
for key in parents:
    outfile2.writelines(str(key)+" "+ " ".join(map(str,parents[key]))+"\n")
outfile2.close()


subsetCount = {}
for key in subsetOf:
    if len(subsetOf[key]) in subsetCount:
        subsetCount[len(subsetOf[key])].append(key)
    else:
        subsetCount[len(subsetOf[key])] = [key]
print "the lists have same number of child trips"
# print subsetCount

outfile3 = open("subsetResults/subsetcount.txt", "w")
for key in subsetCount:
    outfile3.writelines(str(key)+" "+ " ".join(map(str,subsetCount[key]))+"\n")
outfile3.close()

parentCount = {}
for key in parents:
    if len(parents[key]) in parentCount:
        parentCount[len(parents[key])].append(key)
    else:
        parentCount[len(parents[key])] = [key]
print "the lists have same number of parent trips"
# print parentCount

outfile4 = open("subsetResults/parentcount.txt", "w")
for key in parentCount:
    outfile4.writelines(str(key)+" "+ " ".join(map(str,parentCount[key]))+"\n")
outfile4.close()
del parentCount
del parents

# clusterCenters = []
# nodestoConsider = subsetCount[min(subsetCount)]
# clusters = []
# nodesThatAreGoningToBeconds = list(set(nodestoConsider).intersection(set(parentCount[1])))
# print "========================"
# for j in nodesThatAreGoningToBeconds:
#     print j
#     print parents[parents[j][0]]
print "sorted trips accourding to child node count"
print sorted(subsetCount.keys(), reverse=True)
