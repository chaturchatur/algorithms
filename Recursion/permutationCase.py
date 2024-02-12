def permutationSpace(ip, op):
    """Generates all case permutations of a given string"""
    if len(ip) == 0: # Base case 
        print(op)   # print all permutation cases
        return 
    op1 = op + ip[0].lower()
    op2 = op + ip[0].upper()
    ip = ip[1:] #remove first index element
    permutationSpace(ip, op1) # First recursive call: include lower case character
    permutationSpace(ip, op2) # Second recursive call: include upper case character
    return 
    
def main():
    ip = "abc"
    permutationSpace(ip, "")

if __name__ == "__main__":
    main()
