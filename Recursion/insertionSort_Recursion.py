def insert(array, element):
   """Inserts an element into a sorted array."""
   if not array or element >= array[-1]:
       array.append(element)  # Base case: append if empty or at correct position
       return
   last = array.pop()  # Temporarily remove last element
   insert(array, element)  # Recursively insert into smaller array
   array.append(last)  # Reinsert last element in its sorted position

def sortArrayRecursive(array):
   """Sorts an array using insertion sort recursively."""
   if not array:
       return  # Base case: empty array is already sorted
   last = array.pop()  # Remove last element
   sortArrayRecursive(array)  # Sort remaining elements
   insert(array, last)  # Insert last element in its sorted position

def main():
   array = [1, 5, 6, 3, 4, 2]
   print("Before sorting:", array)
   sortArrayRecursive(array)
   print("After sorting:", array)

if __name__ == "__main__":
   main()

