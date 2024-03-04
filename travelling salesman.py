import itertools

def tsp(graph):
    n = len(graph)
    all_vertices = set(range(n))
    
   
    memo = {}

    def tsp_helper(curr, remaining):
        if not remaining:
            return graph[curr][0]  
        
        key = (curr, tuple(remaining))
        if key in memo:
            return memo[key]

        min_cost = float('inf')
        for next_city in remaining:
            cost = graph[curr][next_city] + tsp_helper(next_city, tuple(v for v in remaining if v != next_city))
            min_cost = min(min_cost, cost)

        memo[key] = min_cost
        return min_cost

    return tsp_helper(0, tuple(all_vertices - {0}))


if __name__ == "__main__":
  
    example_graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    result = tsp(example_graph)
    print("Minimum cost for TSP:", result)
