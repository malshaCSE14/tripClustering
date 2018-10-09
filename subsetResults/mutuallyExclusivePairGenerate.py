import itertools

def isPairMutuallyExclusive(trip1, trip2):
    return True

def comb(input, lst = [], lset = set()):
   if lst:
      yield lst
   for i, el in enumerate(input):
      if lset.isdisjoint(el):
         for out in comb(input[i+1:], lst + [el], lset | set(el)):
            yield out

def accrue(u, bset, csets):
    for i, c in enumerate(csets):
        y = u + [c]
        yield y
        boc = bset|c
        ts = [s for s in csets[i+1:] if boc.isdisjoint(s)]
        for v in accrue (y, boc, ts):
            yield v


infile1 = open("subsetcount2.txt", "r")
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

childTrips = {}
infile3 = open("subsets2.txt", "r")
line3 = infile3.readline()
while line3!="":
    tripList = map(int, line3.strip().split(" "))
    childTrips[tripList[0]] = tripList[1:]
    line3 = infile3.readline()

infile3.close()
tripsToCheckInOrder = []
keyConsiderationOrder =  sorted(dictSubSetCount.keys(), reverse=True)
mutuallyExclusivePairs = {}
for key in keyConsiderationOrder:
    tripIndexList = dictSubSetCount[key]
    for index in tripIndexList:
        # tripsToCheckInOrder.append(trips[index])
        tripsToCheckInOrder.append(index)
# print tripsToCheckInOrder
numberOfClusters = 2
clusterNodes = {}
tripNumbersOfClusters = {}
for i in range(numberOfClusters):
    clusterNodes[i] = []
    # tripNumbersOfClusters[i] = []


check = []
#initially add 3 or numberOfClusters trips to the check list
for ind in tripsToCheckInOrder[:numberOfClusters-1]:
    check.append(set(trips[ind]))

# print check

flag = 0
for k in tripsToCheckInOrder[numberOfClusters-1:]:
    check.append(set(trips[k]))
    # print "k", k
    #chech for mutually exclusive sets
    # for c in comb(check):
    #     # print len(c)
    #     if len(c) == numberOfClusters:
    #         # print "c", c
    #         clusterID = 0
    #         for cc in c:
    #
    #             for key, value in trips.items():
    #                 if cc == value:
    #                     clusterNodes[clusterID] = value # initialize the node set of each cluster
    #                     clusterID+=1
    #                     print key
    #                     tripNumbersOfClusters[clusterID] = [key] #store tripNumbers which belong to each cluster; in a dictionary
    #         flag = 1
    #         break
    # if flag == 1:
    #     break

    for c in accrue([], set(), check):
        if len(c) == numberOfClusters:
            # print "c", c
            clusterID = 0
            for cc in c:
                for key, value in trips.items():
                    if cc == set(value):
                        clusterNodes[clusterID] = value # initialize the node set of each cluster
                        print key ,"initial parent trips"
                        tripNumbersOfClusters[clusterID] = [key] #store tripNumbers which belong to each cluster; in a dictionary
                        clusterID += 1
            flag = 1
            break
    if flag == 1:
        break
# print clusterNodes #cluster Nodes have the road segments IDs along the trips

#store parent trip nodes as initial cluster nodes --->done
#store tripNumbers which belong to each cluster; in a dictionary ---> done
#Remove clustered trips from trips dictoinary
#uncomment =========================================
for clusterID in tripNumbersOfClusters:
    parentTripIndex = tripNumbersOfClusters[clusterID][0]
    childTripIndexList = childTrips[parentTripIndex]
    # print len(childTripIndexList)
    trips.pop(parentTripIndex, None)
    for eachChildTripIndex in childTripIndexList:
        # print eachChildTripIndex
        tripNumbersOfClusters[clusterID].append(eachChildTripIndex)
        trips.pop(eachChildTripIndex, None)
print len(trips) , "trips length after removing mutually exclusive trip families"
# print tripNumbersOfClusters

#uncomment -===========================================
# #for each trip; if it intersects with more than one clusters; a trip cut --> remove trip
tripCut = []
for eachTripIndex in trips:
    nodesInTrip = set(trips[eachTripIndex])
    intersectingClustersCount = 0
    for eachClusterID in clusterNodes:
        if set(clusterNodes[eachClusterID]).intersection(set(nodesInTrip)):

            if intersectingClustersCount<2:
                intersectingClustersCount += 1

            # else:
            #     # print "trip ID", eachTripIndex, "intersects cluster", eachClusterID
            #     # tripCut.append(eachTripIndex)  # Add to trip cut count
            #     # trips.pop(eachTripIndex, None)
            #     print "kkkkk"
            #     # break
            # print intersectingClustersCount
            if intersectingClustersCount>=2:
                print "need to pop trip later", eachTripIndex
                tripCut.append(eachTripIndex)  # Add to trip cut count
                # trips.pop(eachTripIndex, None)
print len(tripCut)
#
# # Add to trip cut count
#==================================================================
# #for the remaining trips, starting from the cluster which has smallest trip size, select all the trips with intersection to it
intersectingTripsWithClusters = {}
# for k in clusterNodes:
#     intersectingTripsWithClusters[k] =[]
#     for remainingTrip in trips: # trip index
#         intersection = set(trips[remainingTrip]).intersection(set(clusterNodes[k]))
#         if intersection:
#             remainingLength = len(set(trips[remainingTrip])) - len(intersection)
#             intersectingTripsWithClusters[k].append([remainingLength, remainingTrip])
#=====================================================================
# #add them to the clussters in a way that the trips with smallest length non intersecting part first added to the cluster
# for k in sorted(clusterNodes, key=lambda k: len(clusterNodes[k]), reverse=False): #cluster key eg:1,2,3..
#     maximumNumberOfTripsInACluster = len(max(tripNumbersOfClusters.values(), key=len))
#     print k #k = key of cluster nodes 0, 1, 2
#     sortedTrips = sorted(intersectingTripsWithClusters[k], key= lambda x: x[0]) #are the trips sorted according to length of remaining part?
#     for tripIndex2 in sortedTrips:
#         while len(clusterNodes[k]) <= maximumNumberOfTripsInACluster:
#             tripNumbersOfClusters[k].append(tripIndex2)
#             for roadSegment in trips[tripIndex2]:
#                 if roadSegment not in clusterNodes[k]:
#                     clusterNodes[k].append(roadSegment)
#             trips.pop(tripIndex2, None)
#         else:
#             break

#==========================================================


#untill the trip count is equal or one more
#update the cluster
#for each remaining trip; if more than one intersection with clusters; a trip cut --> remove trip
#do this repeatedly untill no trips left