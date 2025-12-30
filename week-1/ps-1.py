# Challenge 1: Team Contribution Multiplier

# Input Array
contributions = [1, 2, 3, 4]

# Brute Force Approach

def calculateContribution(contributions):
    n = len(contributions)
    impact = [1] * n
    
    for i in range(n):
        for j in range(n):
            if i==j: continue
            impact[i] *= contributions[j]
            
    return impact

print("Brute Force:", calculateContribution(contributions))

# Time Complexity: O(n^2)
# Space Complexity: O(n)

# ------------------------------------------------------------------------------ #

# Optimal Approach

# using prefix & suffix approach to solve the challenge in the optimal time and space.

def calculateContribution2(contributions):
    n = len(contributions)
    impact = [1] * n
    
    # Prefix Product
    prefix = 1
    for i in range(n):
        impact[i] = prefix
        prefix *= contributions[i]
        
    # Suffix Product
    suffix = 1
    for j in range(n-1, -1, -1):
        impact[j] *= suffix
        suffix *= contributions[j]
    
    return impact

print("Optimal (Time & Space):", calculateContribution2(contributions))

# Time Complexity: O(n)
# Space Complexity: O(1)