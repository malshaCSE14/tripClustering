import itertools

def comb(seq):
   for n in range(1, len(seq)):
      for c in itertools.combinations(seq, n): # all combinations of length n
         if len(set.union(*map(set, c))) == sum(len(s) for s in c): # pairwise disjoint?
            yield list(c)
noOfClusters = 3
length = 0
for c in comb([[1, 2, 3], [3, 6, 8], [4, 9], [6, 11], [13,14]]):
    if len(c)==3:
        print c
        break