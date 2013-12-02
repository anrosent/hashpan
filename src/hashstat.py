import sys
from collections import defaultdict
from main import parse_PAN
from util import get_pans_str
from itertools import groupby

def print_dist(dist, title):
    print("%s Distribution"%title)
    total = sum(dist.values())
    for bin, num in sorted(dist.items(), key=lambda x:x[1]):
        print("%s\t|%.3f"%(bin, num/total))

def cond_dists(pans):
    parts = map(parse_PAN, pans)
    #print(list(parts))
    #Groups by IIN
    keyfunc = lambda x:x[0]
    grouped = sorted(parts, key=keyfunc)
    for key, group in groupby(grouped, key=keyfunc):
        print("IIN is %s"%key)
        nhist(map(lambda x:x[1], group), 1)
        
def dists(pans):
    IINs = defaultdict(int)
    UIDs = defaultdict(int)
    checks = defaultdict(int)
    for pan in pans:
        (iin, uid, check) = parse_PAN(pan)
        IINs[iin] += 1
        UIDs[uid] += 1
        checks[check] += 1
    return IINs, UIDs, checks

def nhist(pans, n):
    bins = defaultdict(int)
    for pan in pans:
        for i in range(len(pan)-n+1):
            bins[tuple(pan[i:i+n])] += 1
    for i, h in sorted(bins.items(), key=lambda x:x[-1], reverse=True):
        print("%s|%d"%(i, h))
        
if __name__ == '__main__':
    dists(get_pans_str())