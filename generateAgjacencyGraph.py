import networkx as nx
import operator

G=nx.Graph()
pos=nx.spring_layout(G)

outfile = open("edgeNumbers.txt", "w")
# Generate trip =================================
tripsfileopen = open("trips 2.txt", "r")
line = tripsfileopen.readline()
edgeNo = 1
while line!="":
    tripStrings = line.strip().split(",")[1:]
    a = map(int, tripStrings)
    for nodeIndex in range(1,len(a)):
        if G.has_node(a[nodeIndex-1])== False:
            G.add_node(a[nodeIndex-1])
            # print a[nodeIndex-1], "a[nodeIndex-1] added"
        if G.has_node(a[nodeIndex]) == False:
            G.add_node(a[nodeIndex])
            # print a[nodeIndex], "a[nodeIndex] added"

            #wrong==========================
        if G.has_edge(a[nodeIndex-1], a[nodeIndex]):
            newWeight = int(G.get_edge_data(a[nodeIndex-1], a[nodeIndex])['weight']) + 1
            G.add_edge(a[nodeIndex - 1], a[nodeIndex], weight=newWeight)
            # print "newWeight between ", a[nodeIndex - 1], a[nodeIndex],"is", newWeight
        else:
            G.add_edge(a[nodeIndex-1], a[nodeIndex], weight=1)
            print edgeNo, a[nodeIndex-1], a[nodeIndex]
            outfile.writelines(str(edgeNo)+" "+str(a[nodeIndex-1])+" "+str(a[nodeIndex])+"\n")
            edgeNo+=1
    line = tripsfileopen.readline()
print G.number_of_edges()
print G.number_of_nodes()
print nx.number_connected_components(G)
