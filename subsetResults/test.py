def isPairMutuallyExclusive(trip1, trip2):
    return True

infile1 = open("subsetcount.txt", "r")
dictSubSetCount = {}
line1 = infile1.readline()
while line1!="":
    list1 = map(int, line1.strip().split(" "))
    dictSubSetCount[list1[0]] = list1[1:]
    line1 = infile1.readline()
infile1.close()

infile2 = open("../tripPaths.txt", "r")
trips = {}
tripIndex = 1
line2 = infile2.readline()
while line2!="":
    trips[tripIndex] = map(int, line2.strip().split(" "))
    tripIndex+=1
    line2 = infile2.readline()
infile2.close()

tripsToCheckInOrder = []
keyConsiderationOrder =  sorted(dictSubSetCount.keys(), reverse=True)
mutuallyExclusivePairs = {}
for key in keyConsiderationOrder:
    tripIndexList = dictSubSetCount[key]
    for index in tripIndexList:
        # tripsToCheckInOrder.append(trips[index])
        tripsToCheckInOrder.append(index)
# print tripsToCheckInOrder
for i in range(len(tripsToCheckInOrder)):
    print i
    for j in range(i+1, len(tripsToCheckInOrder)):
        if len(set(trips[tripsToCheckInOrder[i]]).intersection(set(trips[tripsToCheckInOrder[j]])))==0:
            # print tripsToCheckInOrder[i], tripsToCheckInOrder[j], "are mutually exclusive"
            if tripsToCheckInOrder[i] not in mutuallyExclusivePairs:
                mutuallyExclusivePairs[tripsToCheckInOrder[i]] = [tripsToCheckInOrder[j]]
            else:
                mutuallyExclusivePairs[tripsToCheckInOrder[i]].append(tripsToCheckInOrder[j])
            if tripsToCheckInOrder[j] not in mutuallyExclusivePairs:
                mutuallyExclusivePairs[tripsToCheckInOrder[j]] = [tripsToCheckInOrder[i]]
            else:
                mutuallyExclusivePairs[tripsToCheckInOrder[j]].append(tripsToCheckInOrder[i])

print mutuallyExclusivePairs

outfile = open("mutuallyExclusivePairs.txt", "w")
for parent in tripsToCheckInOrder:
    outfile.writelines(" ".join(map(str, mutuallyExclusivePairs[parent])))
outfile.close()