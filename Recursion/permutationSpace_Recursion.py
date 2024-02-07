def permutationSpace(ip, op, start):
    """Generates all permutations of a given string, separating characters with spaces"""
    if len(ip) == 0: # Base case 
        print(start, end="") # print first element : input[0]
        print(op)   # print all permutation space : input[1:]
        return 
    op1 = op + ip[0]
    op2 = op + ' ' + ip[0]
    ip = ip[1:]
    permutationSpace(ip, op1, start) # First recursive call: include character without space
    permutationSpace(ip, op2, start) # Second recursive call: include  character prefixed with space
    return 
    
def main():
    ip = "ABC"
    permutationSpace(ip[1:], "", ip[0])

if __name__ == "__main__":
    main()
