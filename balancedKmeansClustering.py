import random
import networkx as nx

def isSubset(trip, cluster):
    for eachnode in trip:
        if eachnode not in cluster:
            return False
    else:
        return True

numberOfClusters = 2
numberOfNodes = 31880

G=nx.Graph()
G.add_nodes_from(list(range(1, numberOfNodes+1)))
# Generate trip =================================
tripsfileopen = open("tripPaths.txt", "r")
# tripsfileopen = open("sampleTrips.txt", "r")
line = tripsfileopen.readline()
tripDict = {}
alltrips = []
while line!="":
    tripStrings = line.strip().split(" ")
    a = map(int, tripStrings)
    alltrips.append(a)
    for i in range(1, len(a)):
        if a[i-1]<a[i]:
            if tripDict.has_key((a[i-1], a[i])):
                tripDict[(a[i-1], a[i])] +=1
            else:
                tripDict[(a[i - 1], a[i])] = 1
        else:
            if tripDict.has_key((a[i], a[i-1])):
                tripDict[(a[i], a[i-1])] += 1
            else:
                tripDict[(a[i], a[i - 1])] = 1
    line = tripsfileopen.readline()
tripsfileopen.close()
maxtripcount =  float(max(tripDict.values()))

numberOfTrips = len(alltrips)
print "trips read..!"
# adjacencyfileopen = open("Adjacency File 2.txt", "r")
adjacencyfileopen = open("Adjacency File.txt", "r")
line = adjacencyfileopen.readline()
while line!="":
    adjacencyStrings = line.strip().split(" ")
    a = map(int, adjacencyStrings)
    for i in range(1, len(a)):
        if a[0]< a[i]:
            if tripDict.has_key((a[0],a[i])):
                G.add_edge(a[0], a[i], weight = 1.0 - (float(tripDict[(a[0],a[i])])/maxtripcount)) #7004 was there
            else:
                G.add_edge(a[0], a[i], weight = 1.0)
        else:
            if tripDict.has_key((a[i], a[0])):
                G.add_edge(a[i], a[0], weight=1.0 - (float(tripDict[(a[i], a[0])]) / maxtripcount))
            else:
                G.add_edge(a[i], a[0], weight= 1.0)
    line = adjacencyfileopen.readline()
adjacencyfileopen.close()
print "graph created..!"

clusters = {}
# for i in range(numberOfClusters):
#     clusters[i] = []

initialCentroids = random.sample(xrange(1, numberOfNodes+1), numberOfClusters)
print "initial Centroids ", initialCentroids
for i in range(len(initialCentroids)):
    clusters[i] = [initialCentroids[i]]
# Do assign nodes to clusters somehow
for node in range(1, numberOfNodes+1):
    if node not in initialCentroids:
        centroidID = 0
        minDistance = 999
        releventCluster = 999
        for centroid in initialCentroids:
            try:
                val = nx.shortest_path_length(G, node, centroid)
            except nx.exception.NetworkXNoPath:
                val =  99
            if val<minDistance:
                minDistance = val
                releventCluster = centroidID
            centroidID += 1
        clusters[releventCluster].append(node)
        print node, releventCluster


nodesCountPerCluster = {}
for i in range(numberOfClusters):
    nodesCountPerCluster[i] = len(clusters[i])

print "Number of Nodes per Cluster: ", nodesCountPerCluster

noOfTripsPerCluster = {}
#initialization
for key in range(numberOfClusters):
    noOfTripsPerCluster[key] = 0

print "All Trips: ",numberOfTrips

limitOfnoOfTripsPerCluster = float(numberOfTrips)/numberOfClusters
tripCutCount = 0
for trip in alltrips:
    flag = 0 # trip belong to no cluster
    for i in range(numberOfClusters):
        if isSubset(trip, clusters[i]):
            flag =1
            noOfTripsPerCluster[i] +=1
    if flag == 0:
        tripCutCount+=1
print clusters
print "Remaining trips: ", tripCutCount
print "Number Of Trips Per Cluster: ", noOfTripsPerCluster
print "Trip cut percentage: ", tripCutCount * 100.0 / numberOfTrips, "%"