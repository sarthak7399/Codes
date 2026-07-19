# https://leetcode.com/problems/find-all-people-with-secret/

# Example 3:
# Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
# Output: [0,1,2,3,4]
# Explanation:
# At time 0, person 0 shares the secret with person 1.
# At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
# Note that person 2 can share the secret at the same time as receiving it.
# At time 2, person 3 shares the secret with person 4.
# Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # Union-Find parent array
        parent = list(range(n))

        # Track who knows the secret
        know = [False] * n
        know[0] = know[firstPerson] = True

        def find(x):
            # Find with path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            # Union two sets
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        i = 0
        while i < len(meetings):
            t = meetings[i][2]
            temp = []  # People involved at same time

            j = i
            # Process all meetings at time t
            while j < len(meetings) and meetings[j][2] == t:
                union(meetings[j][0], meetings[j][1])
                temp += meetings[j][:2]
                j += 1

            # Propagate secret to connected components
            for x in temp:
                if know[x]:
                    know[find(x)] = True

            # Update individuals based on their component
            for x in temp:
                know[x] |= know[find(x)]

            # Reset parents for next time group
            for x in temp:
                parent[x] = x

            i = j

        # Return all people who know the secret
        return [i for i in range(n) if know[i]]
