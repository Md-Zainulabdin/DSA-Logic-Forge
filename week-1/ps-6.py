# Challenge 6: Tower of Hanoi Algorithm

# using Recursive approach tought by Miss Urooj.

def towerOfHanoi(N, from_rod, to_rod, aux_rod):
    if N <= 0:
        return

    # Base case
    if N == 1:
        print(f"Disk 1 moved from {from_rod} to {to_rod}")
        return

    
    towerOfHanoi(N - 1, from_rod, aux_rod, to_rod)

    print(f"Disk {N} moved from {from_rod} to {to_rod}")

    towerOfHanoi(N - 1, aux_rod, to_rod, from_rod)


# Driver code
towerOfHanoi(3, "A", "B", "C")