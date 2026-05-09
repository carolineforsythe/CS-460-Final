"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Caroline Forsythe
Student ID:   827344993

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return ("A shortest-path run from S is not enough because it will not reach all of the relics and it is not "
            "guaranteed to finish at T, both of which are required. Even though it finds the cheapest route, it likely "
            "does not find the route that fits the requirements within the project. The decision that remains is the "
            "order in which the relics should be visited before reaching the end, T. This requires search over orders "
            "because there are k! sequences in which the relics can be visited in and there isn't a guaranteed greedy "
            "local choice that will find the optimal route.")


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """

    # create variables to track
    # using set for search decreases time complexity
    seen = set()
    sources = []
    for node in [spawn] + list(relics):
        if node not in seen:
            # add node if it is new
            seen.add(node)
            sources.append(node)
    return sources

    pass


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    # initialize distances to infinity
    distance = {node: float('inf') for node in graph}

    # initialize distance to source as 0 b/c it is the starting point
    distance[source] = 0
    heap = [(0, source)]

    while heap:
        # pop the smallest unprocessed node
        cost, u = heapq.heappop(heap)

        # continue if cheaper path already found
        if cost > distance[u]:
            continue

        # explore neighbors
        for v, w in graph[u]:
            newCost = cost + w
            if newCost < distance[v]:
                # found new cheaper path
                distance[v] = newCost
                heapq.heappush(heap, (newCost, v))

    return distance

    pass


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    # get the sources and create table to track distances
    sources = select_sources(spawn, relics, exit_node)
    distanceTable = {}

    # run dijkstra's algorithm on each source node
    for source in sources:
        distanceTable[source] = run_dijkstra(graph, source)

    return distanceTable

    pass


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return ("Because S only holds the guaranteed smallest distances, any dist[v] in S will be the most optimal path. No "
            "later discovered path can be better. dist[u] holds the shortest path found so far for nodes not yet "
            "finalized, and updates if path is found that is shorter than what is currently stored in dist[u]. It only "
            "considers routes that pass through nodes in the finalized set S. At initialization, the only known node is "
            "the source node and the distance cost is 0, because it is the current location of the torchbearer. All "
            "other nodes are set to inf() because paths to them have not been explored yet. Thus, the invariant holds at "
            "initialization. The algorithm always picks the non-finalized node with the shortest distance in dist[u]. "
            "Due to the fact that there are no negative edge weights (edge weights only go from 0-infinity), any "
            "alternative path will be equal to or greater than the one stored in dist[u]. This means that the distance "
            "is optimal, and finalizing the node holds the invariant. When the heap is empty, all reachable nodes have "
            "been added to S, and dist[v] holds the actual shortest path for every node. Unreachable remain set to inf() "
            "The invariant holds. Connecting correct distances leads to correct routing decisions because it ensures "
            "that the path taken by the torchbearer is the shortest, lowest cost option that avoids wasting fuel, taking "
            "long paths, and possibly getting stuck in a dead end (because the paths are directed).")


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return ("A greedy solution always chooses the shortest immediate path, ignoring how that affects the overall route "
            "cost. We will use the concrete illustration provided earlier in the document for a counterexample. There "
            "are two possible 'optimal' routes to choose from, one results in a total cost of 4 and the other has a "
            "total cost of 5. The greedy solution selects S -> B -> D -> C -> T, with a total cost of 4. It starts by "
            "choosing B from S because S -> B = 1 and S -> C = 2. S -> B is the more optimal local solution. The optimal "
            "solution picks S -> B -> D -> C -> T, with a total cost of 4. Greedy choices can lead to costly future "
            "decisions because the locally cheap option might not be a part of the locally optimal solution. The "
            "algorithm must explore every possible order in which the relics can be visited by the torchbearer to "
            "determine the most optimal path.")


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    # make sure explain_problem() prints and is passed thru properly
    description = explain_problem()
    print(description)

    # test select_sources()
    sources = select_sources('S', ['R1', 'R2', 'S'], 'T')
    print(sources)

    # copied graphs for testing
    graphTest = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    graphTest2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    source = 'S'
    exitNode = 'T'
    relics = ['B', 'C', 'D']

    #test run_dijkstra()
    print(run_dijkstra(graphTest, source))

    # test precompute_distances()
    print(precompute_distances(graphTest, source, relics, exitNode))

    # make sure dijkstra_invariant_check() prints and is passed thru properly
    print(dijkstra_invariant_check())

    # make sure explain_search() prints and is passed thru properly
    print(explain_search())




    #_run_tests()
