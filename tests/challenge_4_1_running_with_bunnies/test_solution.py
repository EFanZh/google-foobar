from unittest import TestCase

from challenge_4_1_running_with_bunnies import solution


class SolutionTestCase(TestCase):
    def test_all_pairs_shortest_path(self):
        infinity = float('inf')

        test_cases = [
            ([[0, infinity, -2, infinity],
              [4, 0, 3, infinity],
              [infinity, infinity, 0, 2],
              [infinity, -1, infinity, 0]],
             [0, -1, -2, 0,
              4, 0, 2, 4,
              5, 1, 0, 2,
              3, -1, 1, 0]),
        ]

        for matrix, expected in test_cases:
            self.assertEqual(expected, solution.all_pairs_shortest_path(matrix=matrix))

    def test_solution(self):
        test_cases = [
            (([[0, 2, 2, 2, -1],
               [9, 0, 2, 2, -1],
               [9, 3, 0, 2, -1],
               [9, 3, 2, 0, -1],
               [9, 3, 2, 2, 0]],
              1),
             [1, 2]),
            (([[0, 1, 1, 1, 1],
               [1, 0, 1, 1, 1],
               [1, 1, 0, 1, 1],
               [1, 1, 1, 0, 1],
               [1, 1, 1, 1, 0]],
              3),
             [0, 1]),
            (([[0, 1, 1, 1, 1],
               [1, 0, 1, 1, 1],
               [1, 1, 0, 1, 1],
               [1, 1, 1, 0, 1],
               [1, 1, 1, 1, 0]],
              1),
             []),
            (([[0, -2, 1, 1, 1],
               [1, 0, 1, 1, 1],
               [1, 1, 0, 1, 1],
               [1, 1, 1, 0, 1],
               [1, 1, 1, 1, 0]],
              3),
             [0, 1, 2]),
            (([[0, 2],
               [1, 0]],
              3),
             [])
        ]

        for (times, times_limit), expected in test_cases:
            self.assertEqual(expected, solution.solution(times=times, times_limit=times_limit))
