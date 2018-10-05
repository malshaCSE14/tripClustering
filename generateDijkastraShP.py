import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()
# pos=nx.spring_layout(G)
G.add_nodes_from(list(range(1, 31881)))

# Generate trip =================================
tripsfileopen = open("tripPaths.txt", "r")
line = tripsfileopen.readline()
tripDict = {}
while line!="":
    tripStrings = line.strip().split(" ")
    a = map(int, tripStrings)
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
# print tripDict
#
# print max(tripDict.values()), max(tripDict.items(), key=operator.itemgetter(1))[0]


adjacencyfileopen = open("Adjacency File.txt", "r")
line = adjacencyfileopen.readline()
# max = 0
while line!="":
    adjacencyStrings = line.strip().split(" ")
    a = map(int, adjacencyStrings)
    # print a
    for i in range(1, len(a)):
        if a[0]< a[i]:
            if tripDict.has_key((a[0],a[i])):
                G.add_edge(a[0], a[i], weight = 1.0 - (float(tripDict[(a[0],a[i])])/7004.0))
                # if max < float(tripDict[(a[0],a[i])]):
                #     max = float(tripDict[(a[0],a[i])])
            else:
                G.add_edge(a[0], a[i], weight = 1.0)
        else:
            if tripDict.has_key((a[i], a[0])):
                G.add_edge(a[i], a[0], weight=1.0 - (float(tripDict[(a[i], a[0])]) / 7004.0))
                # if max < float(tripDict[(a[i], a[0])]):
                #     max = float(tripDict[(a[i], a[0])])
            else:
                G.add_edge(a[i], a[0], weight= 1.0)
    line = adjacencyfileopen.readline()
adjacencyfileopen.close()

# print max
# nx.draw(G, with_labels = True)
# plt.show()
# generate dijkastra shortest path lengths

print nx.number_connected_components(G)
p = list(nx.connected_components(G))
print p
q = list(nx.connected_component_subgraphs(G))
print q
# ======================== uncomment below section
# di = open("dijkstraShortestPathPickMe.txt", "w")
# for i in range(1, 31881):
#     line = []
#     for j in range(1, 31881):
#         # print "==========="
#         try:
#             val = nx.dijkstra_path_length(G, i, j)
#             line.append(str(val))
#         except nx.exception.NetworkXNoPath:
#             val =  99
#             line.append(str(val))
#     di.writelines(" ".join(line))
#     print "line", i, "printed"
#     di.writelines("\n")