"""
Dynamic Programming Approach -> It gives the optimal distance but takes little  space.
I'm using bitmask to track visited cities , It's faster than real values.
"""

# Distances from one branch to another branch --> Calculated using haversine method.
g = [[0, 2.39, 4.44, 0.73, 5.51, 5.1, 1.24, 1.21, 5.5, 6.64],
     [2.39, 0, 2.09, 1.87, 3.19, 2.74, 1.35, 2.11, 3.18, 4.28],
     [4.44, 2.09, 0, 3.96, 1.83, 0.66, 3.43, 3.87, 1.83, 2.2],
     [0.73, 1.87, 3.96, 0, 4.88, 4.61, 0.57, 1.52, 4.88, 6.15],
     [5.51, 3.19, 1.83, 4.88, 0, 1.63, 4.31, 5.26, 0.01, 2.12],
     [5.1, 2.74, 0.66, 4.61, 1.63, 0, 4.08, 4.51, 1.64, 1.54],
     [1.24, 1.35, 3.43, 0.57, 4.31, 4.08, 0, 1.66, 4.31, 5.6],
     [1.21, 2.11, 3.87, 1.52, 5.26, 4.51, 1.66, 0, 5.26, 6.03],
     [5.5, 3.18, 1.83, 4.88, 0.01, 1.64, 4.31, 5.26, 0, 2.13],
     [6.64, 4.28, 2.2, 6.15, 2.12, 1.54, 5.6, 6.03, 2.13, 0]]


n = 10  # Count of cities
visited = (1 << n) - 1
dp = [[-1] * n for _ in range(visited + 1)]   # We know that number of distinct possible combinations is 2^n


def tsp(mask, pos):
    if mask == visited:
        return g[pos][0], [pos, 0]

    # Lookup case if already calculated
    if dp[mask][pos] != -1:
        return dp[mask][pos]

    # Loop through unvisited cities
    ans = float('inf')
    path = []

    for city in range(n):
        if mask & (1 << city) == 0:
            new_ans, new_path = tsp(mask | (1 << city), city)
            new_ans += g[pos][city]

            if new_ans < ans:
                ans = new_ans
                path = [pos] + new_path

    dp[mask][pos] = ans, path
    return ans, path


total_distance, path = tsp(1, 0)
print('Distance is:', total_distance, 'km')

city_list = ['Uttara Branch', 'City Bank Airport', 'City Bank Nikunja', 'City Bank Beside Uttara Diagnostic',
             'City Bank Mirpur 12', 'City Bank Le Meridien', 'City Bank Shaheed Sarani', 'City Bank Narayanganj',
             'City Bank Pallabi', 'City Bank JFP']

path_names = [city_list[index] for index in path]

print(f"Route is: {' >> '.join(path_names)}")

# Write to output file

f = open("output.txt", 'w')
f.writelines(f"Total Distance is : {total_distance} km \n")
f.writelines(f"Route is : {' >> '.join(path_names)}")
f.close()
print()

print("Output written at output.txt file.")