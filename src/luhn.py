#Luhn Checksum Algorithm stuff 

def digits(n):
    return list(map(int, str(n)))
    
def luhn_check(pan):
    ds = digits(str(pan))
    check = sum(ds[-1::-2])
    for d in ds[-2::-2]:
        check += sum(digits(d*2))
    return check % 10
    
def luhn_valid(pan):
    return not luhn_check(pan) 
    
def luhn_calc(pan):
    check = luhn_check(int(str(pan) + '0'))
    return 10 - check if check else check
    
def validate_luhns():
    import sys
    for pan in map(lambda x:x.strip(), sys.stdin.readlines()):
        print(pan[-1] == str(luhn_calc(str(pan)[:-1])))
        
if __name__ == '__main__':
    validate_luhns()