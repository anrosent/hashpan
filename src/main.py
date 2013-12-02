import sys
from os.path import join
from base64 import b64encode
from hashlib import sha1

guess_generator = None

#returns (IIN, uid, Luhn checksum)
def parse_PAN(pan):
    return (pan[:6], pan[6:-1], pan[-1])
    
def get_guess_generator(method):
    import guess_generators
    global guess_generator
    try:
        guess_generator = eval('guess_generators.%s'%method)
    except ImportError:
        guess_generator = guess_generators.brute_force

def get_hashes():
    with open(join('..', 'data', 'pan_hashes.txt'),'r') as hash_f:
        return set(map(lambda x:x.strip(), hash_f))
    
def encode(pan):
    return b64encode(sha1(bytes(pan,'ascii')).digest()).decode('ascii')
    
def test_method(test_hashes, outfile):
    with open(outfile, 'w') as cracked_f:
        correct = 0
        total = len(test_hashes)
        for guess_plain in guess_generator():
            guess_hash = encode(guess_plain)
            if guess_hash in test_hashes:
                cracked_f.write('%s:%s'%(guess_hash,guess_plain))
                print('Cracked: %s -> %s'%(guess_hash, guess_plain))
                correct += 1
        print("Summary: %d/%d Cracked"%(correct, total))    
    
if __name__ == '__main__':
    if len(sys.argv) == 2:   
        get_guess_generator(sys.argv[1])
    test_hashes = get_hashes()
    test_method(test_hashes, 'cracks.txt')
    
    