import sys
from os.path import join
from luhn import luhn_calc
from util import get_pans_str
from hashstat import dists

def read_file(f):
    return list(map(lambda x:x.strip(), f))

#####################################################################
#Cheating implementation that tests agaisnt given PANs, not hashes
#   we are supposed to crack
def cheat_base():
            
    def cheat_crack(hash):
        if hash in cache:
            return cache[hash]
        else:
            return hash
    return cheat_crack
    
cheat = cheat_base()          

######################################################################

def uid_gen(iin):
    for uid in range(10**10):
        base = '%s%.9d'%(iin, uid)
        yield base + str(luhn_calc(base))

def iin_sort():
    pans = get_pans_str()
    (IINs, _, _) = dists(pans)
    for iin in sorted(IINs, key=lambda k:IINs[k], reverse=True):
        for pan in uid_gen(iin):
            yield pan
        