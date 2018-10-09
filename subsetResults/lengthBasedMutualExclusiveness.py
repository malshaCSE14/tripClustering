import itertools


# def comb(input, lst = [], lset = set()):
#    if lst:
#       yield lst
#    for i, el in enumerate(input):
#       if lset.isdisjoint(el):
#          for out in comb(input[i+1:], lst + [el], lset | set(el)):
#             yield out
def remainingTailLenghtsList(clusterID):
    intersectingTripsWithClusters = []
    for remainingTrip in trips:  # trip index
        intersection = set(trips[remainingTrip]).intersection(set(clusterNodes[clusterID]))
        if intersection:
            remainingLength = len(set(trips[remainingTrip])) - len(intersection)
            intersectingTripsWithClusters.append([remainingLength, remainingTrip])
    # return intersectingTripsWithClusters
    return sorted(intersectingTripsWithClusters, key= lambda x: x[0])

def addTripToCluster(trip, clusterID, trips, clusterNodes):
    tripSet = set(trips[trip])
    clusterSet  =set(clusterNodes[clusterID])
    return list(tripSet.union(clusterSet))

def addChildern(parent, clusterID, trips, clusterNodes):
    addedChildern = []
    for eachChild in childTrips[parent]:
        try:
            tripSet = set(trips[eachChild])
            clusterSet = set(clusterNodes[clusterID])
            if tripSet.issubset(clusterSet):
                addedChildern.append(eachChild)
        except KeyError:
            pass #child already added

    print len(addedChildern), "addedChildCOunt"
    return addedChildern



def accrue(u, bset, csets):
    for i, c in enumerate(csets):
        y = u + [c]
        yield y
        boc = bset|c
        ts = [s for s in csets[i+1:] if boc.isdisjoint(s)]
        for v in accrue (y, boc, ts):
            yield v

def getTripCutOfAdding(trip, cluster,trips, clusterNodes):
    #add trip's nodes to cluster i and modify only the relevent cluster,, instead of using clusterNodes
    modifiedClusterSets = {}
    for eachcluster in clusterNodes:
        if eachcluster == cluster:
            modifiedClusterSets[eachcluster] = set(clusterNodes[eachcluster]).union(set(trips[trip]))
        else:
            modifiedClusterSets[eachcluster] = set(clusterNodes[eachcluster])

    # print trip, "is gonna be added to ", cluster
    tripCut = []
    for eachTripIndex in trips:
        nodesInTrip = set(trips[eachTripIndex])
        intersectingClustersCount = 0
        for eachClusterID in modifiedClusterSets:
            if set(modifiedClusterSets[eachClusterID]).intersection(set(nodesInTrip)):
                if intersectingClustersCount < 2:
                    intersectingClustersCount += 1
                if intersectingClustersCount >= 2:
                    tripCut.append(eachTripIndex)  # Add to trip cut count
    return tripCut

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
# for ind in tripsToCheckInOrder[:numberOfClusters-1]:
#     check.append(set(trips[ind]))

# print check

flag = 0
# for k in tripsToCheckInOrder[numberOfClusters-1:]:
for k in sorted(trips, key=lambda k: len(set(trips[k])), reverse=True):
    print len(set(trips[k])),"length of", k
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
                        clusterNodes[clusterID] = list(set(value)) # initialize the node set of each cluster
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
                # print "need to pop trip later", eachTripIndex
                tripCut.append(eachTripIndex)  # Add to trip cut count
                # trips.pop(eachTripIndex, None)
print len(tripCut), "trip cut"
for triptoremove in tripCut:
    trips.pop(triptoremove, None)
print len(trips), "length after removing common trips"
#
# # Add to trip cut count
#==================================================================
# #for the remaining trips, starting from the cluster which has smallest trip size, select all the trips with intersection to it
intersectingTripsWithClusters = {}
for k in clusterNodes:
    intersectingTripsWithClusters[k] =[]
    for remainingTrip in trips: # trip index
        intersection = set(trips[remainingTrip]).intersection(set(clusterNodes[k]))
        if intersection:
            remainingLength = len(set(trips[remainingTrip])) - len(intersection)
            intersectingTripsWithClusters[k].append([remainingLength, remainingTrip])
# print intersectingTripsWithClusters
#=====================================================================
# #add them to the clussters in a way that the trips with smallest length non intersecting part first added to the cluster

tailDistanceFromCLuster = {}
# for k in sorted(clusterNodes, key=lambda k: len(clusterNodes[k]), reverse=False): #cluster key eg:2,1,3..
for k in clusterNodes: #cluster key eg:1,2,3..
    tailDistanceFromCLuster[k] = sorted(intersectingTripsWithClusters[k], key= lambda x: x[0]) #trips are sorted according to length of remaining part?




#--------------------------------------------------------------------------










k=min(tripNumbersOfClusters, key=lambda k: len(tripNumbersOfClusters[k])) # cluster key eg:2,1,3..
while len(tripNumbersOfClusters[k]) <= len(max(tripNumbersOfClusters.values(), key=len))+1:
    maxTolerableTripCut = 0
    storeTripCuts = {}
    for eachTripDetail in remainingTailLenghtsList(k): #sorted according to tail length
        cuttingTrips = getTripCutOfAdding(eachTripDetail[1], k, trips, clusterNodes)
        tripCutMeasure = len(cuttingTrips)
        if tripCutMeasure<=maxTolerableTripCut:

            print tripCutMeasure, "trips are cut since", eachTripDetail[1], "added"
            tripNumbersOfClusters[k].append(eachTripDetail[1])
            clusterNodes[k] = addTripToCluster(eachTripDetail[1], k, trips, clusterNodes)
            tails = remainingTailLenghtsList(
                k)  # and we need to calculate distance from here # then sort the distance,..
            # print tails
            # make it the trip which is to be removed next
            trips.pop(eachTripDetail[1], None)
            children = addChildern(eachTripDetail[1], k, trips,
                                   clusterNodes)  # add its children, update tripNumbersOfClusters[k] and clusterNodes[k] too
            tripNumbersOfClusters[k] += children
            for child in children:
                trips.pop(child, None)
            tripCut += cuttingTrips

            print "1 trip added"
            break
        else:
            print "line 261"
            if tripCutMeasure in storeTripCuts:
                storeTripCuts[tripCutMeasure].append(eachTripDetail[1])
            else:
                storeTripCuts[tripCutMeasure] =[eachTripDetail[1]]
    else:
        maxTolerableTripCut = min(storeTripCuts.keys())


    if len(trips) == 0:
        break
    k = min(tripNumbersOfClusters, key=lambda k: len(tripNumbersOfClusters[k]))  # cluster key eg:2,1,3..




    # sortedTripsDetails = tailDistanceFromCLuster[k]
    # for eachTripDetail in sortedTripsDetails:
    #     if len(tripNumbersOfClusters[k])>=maximumNumberOfTripsInACluster:
    #         break
    #
    #     if tripCutMeasure in storeTripCuts:
    #         storeTripCuts[tripCutMeasure].append(eachTripDetail[1])
    #     else:
    #         storeTripCuts[tripCutMeasure]= [eachTripDetail[1]]
    #     # print storeTripCuts.keys()
    #     if tripCutMeasure<=maxTolerableTripCut:
    #         print tripCutMeasure, "trips are cut since", eachTripDetail[1], "added"
    #         tripNumbersOfClusters[k].append(eachTripDetail[1])
    #         clusterNodes[k] = addTripToCluster(eachTripDetail[1], k,trips, clusterNodes)
    #         tails = remainingTailLenghtsList(k)# and we need to calculate distance from here # then sort the distance,..
    #         print tails
    #         #make it the trip which is to be removed next
    #         trips.pop(eachTripDetail[1], None)
    #         children= addChildern(eachTripDetail[1], k, trips, clusterNodes) #add its children, update tripNumbersOfClusters[k] and clusterNodes[k] too
    #         tripNumbersOfClusters[k]+=children
    #         for child in children:
    #             trips.pop(child, None)
    #         tripCut+=cuttingTrips
    #     # else:
    #     #     storeTripCuts.pop(maxTolerableTripCut,None) # are you sure that the values of minimum key are over?
    #     #     maxTolerableTripCut = min(storeTripCuts.keys())
    #     #     print maxTolerableTripCut, "mttc"


    print "done for clusr", k
    print len(tripNumbersOfClusters[k])
print len(trips)































# for k in sorted(clusterNodes, key=lambda k: len(tripNumbersOfClusters[k]), reverse=False):  # cluster key eg:2,1,3..
#     maximumNumberOfTripsInACluster = len(max(tripNumbersOfClusters.values(), key=len))
#     storeTripCuts = {}
#     maxTolerableTripCut = 0
#     sortedTripsDetails = tailDistanceFromCLuster[k]
#     for eachTripDetail in sortedTripsDetails:
#         if len(tripNumbersOfClusters[k])>=maximumNumberOfTripsInACluster:
#             break
#         cuttingTrips = getTripCutOfAdding(eachTripDetail[1], k,trips, clusterNodes)
#         tripCutMeasure = len(cuttingTrips)
#         if tripCutMeasure in storeTripCuts:
#             storeTripCuts[tripCutMeasure].append(eachTripDetail[1])
#         else:
#             storeTripCuts[tripCutMeasure]= [eachTripDetail[1]]
#         # print storeTripCuts.keys()
#         if tripCutMeasure<=maxTolerableTripCut:
#             print tripCutMeasure, "trips are cut since", eachTripDetail[1], "added"
#             tripNumbersOfClusters[k].append(eachTripDetail[1])
#             clusterNodes[k] = addTripToCluster(eachTripDetail[1], k,trips, clusterNodes)
#             tails = remainingTailLenghtsList(k)# and we need to calculate distance from here # then sort the distance,..
#             print tails
#             #make it the trip which is to be removed next
#             trips.pop(eachTripDetail[1], None)
#             children= addChildern(eachTripDetail[1], k, trips, clusterNodes) #add its children, update tripNumbersOfClusters[k] and clusterNodes[k] too
#             tripNumbersOfClusters[k]+=children
#             for child in children:
#                 trips.pop(child, None)
#             tripCut+=cuttingTrips
#         # else:
#         #     storeTripCuts.pop(maxTolerableTripCut,None) # are you sure that the values of minimum key are over?
#         #     maxTolerableTripCut = min(storeTripCuts.keys())
#         #     print maxTolerableTripCut, "mttc"
#
#
#     print "done for clusr", k
#     print len(tripNumbersOfClusters[k])
# print len(trips)

#
#
#
#




















#     sortedTrips = sorted(intersectingTripsWithClusters[k], key=lambda x: x[0])  # are the trips sorted according to length of remaining part?
#     print sortedTrips
#     tailDistanceFromCLuster[k] = sortedTrips


    #can we seperate from here?
 #BTW intersectingTripsWithClusters doesn't contain trips which intersecting with both, coz they are already removed
 #we can keep removing trips which intersect with more than 1 trip. remove trip. add to trip cut

    # for detail in sortedTrips:
    #     while len(clusterNodes[k]) <= maximumNumberOfTripsInACluster+1:
#need to sort them by the number of trips that can be included when it is added. -->ascending or descending?
#             tripNumbersOfClusters[k].append(detail[1])
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