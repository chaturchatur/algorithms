def Hanoi(source, destination, helper, number):
    """Moves the tower of Hanoi disks from the source rod to the destination rod using the helper rod."""
    if number == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    Hanoi(source, helper, destination, number - 1)
    print(f"Move disk {number} from {source} to {destination}")
    Hanoi(helper, destination, source, number - 1)

def main():
    number_of_disks = 3  # Change this to the desired number of disks
    Hanoi("A", "C", "B", number_of_disks)  # Provide the required arguments

if __name__ == "__main__":
    main()
