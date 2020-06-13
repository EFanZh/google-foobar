from unittest import TestCase

from challenge_4_2_free_the_bunny_prisoners import solution


class SolutionTestCase(TestCase):
    def test_solution(self):
        test_cases = [
            ((1, 1), [[0]]),
            ((2, 1), [[0], [0]]),
            ((2, 2), [[0], [1]]),
            ((3, 1), [[0], [0], [0]]),
            ((3, 2), [[0, 1], [0, 2], [1, 2]]),
            ((3, 3), [[0], [1], [2]]),
            ((4, 1), [[0], [0], [0], [0]]),
            ((4, 2), [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]),
            ((4, 3), [[0, 1, 2], [0, 3, 4], [1, 3, 5], [2, 4, 5]]),
            ((4, 4), [[0], [1], [2], [3]]),
            ((5, 1), [[0], [0], [0], [0], [0]]),
            ((5, 2), [[0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 3, 4], [0, 2, 3, 4], [1, 2, 3, 4]]),
            ((5, 3),
             [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]])
        ]

        for (num_buns, num_required), expected in test_cases:
            self.assertEqual(expected, solution.solution(num_buns=num_buns, num_required=num_required))
