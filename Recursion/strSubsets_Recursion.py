def strSubsets(op, ip):
    """Generates all subsets of a given string recursively."""
    if len(ip) == 0: #if input empty -> print current subset
        print(op)
        return
    
    strSubsets(op, ip[1:]) #exclude first character
    strSubsets(op + ip[0], ip[1:]) #include first character
    
def main():
    string = "abc"
    strSubsets("", string)
    
if __name__ == "__main__":
    main()