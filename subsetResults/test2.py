# #!/usr/bin/python
# from random import sample, seed
# import time
# nsets,   ndelta,  ncount, setsize  = 200, 200, 5, 6
# topnum, ranSeed, shoSets, shoUnion = 20, 1234, 0, 0
# seed(ranSeed)
# # print 'Set size = {:3d},  Number max = {:3d}'.format(setsize, topnum)
# #
# # for casenumber in range(ncount):
# #     t0 = time.time()
# #     sets, sizes, ssum = [], [0]*nsets, [0]*(nsets+1);
# #     for i in range(nsets):
# #         sets.append(set(sample(xrange(topnum), setsize)))
# #
# #     if shoSets:
# #         print 'sets = {},  setSize = {},  top# = {},  seed = {}'.format(
# #             nsets, setsize, topnum, ranSeed)
# #         print 'Sets:'
# #         for s in sets: print s
# #
# #     # Method by jwpat7
# def accrue(u, bset, csets):
#     for i, c in enumerate(csets):
#         y = u + [c]
#         yield y
#         boc = bset|c
#         ts = [s for s in csets[i+1:] if boc.isdisjoint(s)]
#         for v in accrue (y, boc, ts):
#             yield v
#     #
#     # # Method by NPE
#     # def comb(input, lst = [], lset = set()):
#     #     if lst:
#     #         yield lst
#     #     for i, el in enumerate(input):
#     #         if lset.isdisjoint(el):
#     #             for out in comb(input[i+1:], lst + [el], lset | set(el)):
#     #                 yield out
#     #
#     # # Uncomment one of the following 2 lines to select method
#     # # for u in comb (sets):
# sets = [set([1,2,3,4,5]), set([5,6,7,8,9]), set([10,11,12,13]), set([23,534,131])]
# for u in accrue ([], set(), sets):
#     # print "sets===================================="
#     # print sets
#     # print "u======================================="
#     if len(u)==3:
#         print u #------------------------------- this is the output
#         break
#     #     sizes[len(u)-1] += 1
#     #     if shoUnion: print u
#     # t1 = time.time()
#     # for t in range(nsets-1, -1, -1):
#     #     ssum[t] = sizes[t] + ssum[t+1]
#     # print '{:7.3f}s  Sizes:'.format(t1-t0), [s for (s,t) in zip(sizes, ssum) if t>0]
#     # nsets += ndelta
lokuekkena = [14498, 7803, 2300, 2299, 2298, 2297, 2296, 2295, 2294, 2293, 2292, 2291, 2290, 2289, 2288, 2287, 435, 436, 437, 438, 439, 440]
podiekkena = [14498, 7803, 2300, 2299]
print set(podiekkena).issubset(lokuekkena)