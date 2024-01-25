def midDel(stack):
    """Removes the middle element from a stack."""
    if not stack:
        return  # Stack is empty, nothing to remove

    mid = (len(stack) + 1) // 2  # Calculate middle element index (rounds up for odd stacks)
    solve(stack, mid)  # Recursively remove element at that index


def solve(stack, k):
    """Recursively removes element at specified index from the stack."""
    if k == 1:
        stack.pop()  # Base case: remove middle element
        return
    top = stack.pop()  # Temporarily store top element
    solve(stack, k - 1)  # Move elements below middle element up
    stack.append(top)  # Put stored element back above the "shifted" elements


def main():
    stack = [1, 5, 6, 3, 4, 2]
    print("Before:", stack)
    midDel(stack)
    print("After:", stack)

if __name__ == "__main__":
    main()
