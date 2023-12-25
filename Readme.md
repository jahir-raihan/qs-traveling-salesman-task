# Traveling Salesman Problem

The problem is simple to understand but hard to interpret. As Naive and bruteforce approaches can lead to `O(n!)` Time complexity. That's why I've used Top-Down Approach with memoization, in simple term Dynamic Programming Approach. 

Now the time complexity is reduced to `O(2^n)` in worst case scenario.

## Haversine Formula 

I've used haversine formula to get distance between all the geolocations provided using latitude and longitude.

**Formula**
```
φ --> Latitude & λ --> Longitude
And R = Radius of earth in km.

a = sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)
c = 2 * atan2( √a, √(1−a) )
d = R ⋅ c
```

# Output

### To run just type out

```bash
python3 traveling-salesman-problem-solution.py
```

## Output is at `output.txt` file.