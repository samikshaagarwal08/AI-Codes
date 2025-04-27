# Function to solve Tower of Hanoi problem
def tower_of_hanoi(n, source, destination, auxiliary):
    # Base case: If only one disk is left, move it directly to the destination
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move top n-1 disks from source to auxiliary, using destination as auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    # Move the n-1 disks from auxiliary to destination, using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Example usage
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')  # A, B, C are the rods
