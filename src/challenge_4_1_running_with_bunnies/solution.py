import itertools


def all_pairs_shortest_path(matrix):
    """
    https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm.
    """

    nodes = len(matrix)
    cache = [num for row in matrix for num in row]
    temp_cache = [0] * (nodes * nodes)

    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                temp_cache[nodes * i + j] = min(cache[nodes * i + j], cache[nodes * i + k] + cache[nodes * k + j])

        cache, temp_cache = temp_cache, cache

    return cache


def solution(times, times_limit):
    nodes = len(times)
    total_bunnies = nodes - 2
    shortest_paths = all_pairs_shortest_path(times)

    if any(shortest_paths[nodes * i + i] < 0 for i in range(nodes)):
        return list(range(total_bunnies))
    else:
        for num_selected_bunnies in range(total_bunnies, 0, -1):
            for selected_bunnies in itertools.combinations(range(total_bunnies), num_selected_bunnies):
                for bunny_path in itertools.permutations(selected_bunnies):
                    length = 0
                    last_node = 0

                    for bunny in bunny_path:
                        bunny_node = bunny + 1
                        length += shortest_paths[nodes * last_node + bunny_node]
                        last_node = bunny_node

                    length += shortest_paths[nodes * last_node + nodes - 1]

                    if length <= times_limit:
                        return list(selected_bunnies)

        return []
