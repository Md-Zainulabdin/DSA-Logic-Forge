# Challenge 5: Fix the Broken Expression

# using BFS approach explained in Friday Session - 01.

from collections import deque

def fixBrokenExpression(expr):
    
    # checking validity
    def isValid(string):
        count = 0
        for ch in string:
            if ch == '(':
                count += 1
            elif ch == ')':
                if count == 0:
                    return False
                count -= 1
        return count == 0
    

    queue = deque([expr]) # using queue to pop form left in constant time
    visited = set([expr]) # using set to avoid duplicates
    
    result = []
    found = False

    while queue:
        curr = queue.popleft()

        if isValid(curr):
            result.append(curr)
            found = True

        if found:
            continue

        for i in range(len(curr)):
            if curr[i] not in "()":
                continue

            next_str = curr[:i] + curr[i + 1:]

            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)

    return result

input = "()())()"
print("Valid Expressions:",fixBrokenExpression(input))