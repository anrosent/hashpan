import sys

def get_pans():
    with open('../data/pans.txt','r') as pans_f:
        return list(map(lambda x:int(x.strip()), pans_f))
        
def get_pans_str():
    with open('../data/pans.txt','r') as pans_f:
        return list(map(lambda x:x.strip(), pans_f))        
    
def get_hashes():
    with open('../data/pans.txt', 'r') as hashes_f:
        return list(map(lambda x:x.strip(), hashes_f))
    