def insert(array, element):
    if len(array) == 0 or array[-1] <= element:
        array.append(element)
        return
    last = array.pop()  # Remove and store the last element
    insert(array, element)  # Recursively insert element into smaller array
    array.append(last)  # Reinsert the last element

def sortArrayRecursive(array):
    if len(array) == 0:
        return
    last = array.pop()
    sortArrayRecursive(array)
    insert(array, last)

def main():
    array = [1,5,6,3,4,2]  # Convert input to numbers
    print("Before sorting:", array)
    sortArrayRecursive(array)
    print("After sorting:", array)

if __name__ == "__main__":
    main()
