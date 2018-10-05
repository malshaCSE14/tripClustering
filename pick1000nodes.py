infile= open("tripPaths.txt" ,"r")
outfile = open("sampleTrips.txt", "w")
line = infile.readline()
count = 0
while line!="":
    nodes = map(int, line.strip().split(" "))
    if all(i <= 3000 for i in nodes):
        outfile.writelines(line)
        # outfile.writelines("\n")
        count+=1
    line = infile.readline()
infile.close()
print count
outfile.close()