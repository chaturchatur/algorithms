def reverseStack(stack):
   """Reverses the order of elements in a stack using recursion."""
   if len(stack) == 1: # Base case: stack with only one element is already reversed.
       return stack
   top = stack.pop()  # Remove the top element from the stack.
   reverseStack(stack)  # Recursively reverse the remaining elements.
   insert(stack, top)  # Insert the removed element back onto the stack.


def insert(stack, ele):
   """Inserts an element into a stack, maintaining its order."""
   if len(stack) == 0: # Base case: empty stack, simply append the element.
       stack.append(ele)
       return
   top = stack.pop()  # Temporarily remove the top element.
   insert(stack, ele)  # Recursively insert the element into the smaller stack.
   stack.append(top)  # Put the removed element back on top.


def main():
   array = [1, 5, 6, 3, 4, 2]
   print("Before reversal:", array)
   reverseStack(array)
   print("After reversal:", array)


if __name__ == "__main__":
   main()
