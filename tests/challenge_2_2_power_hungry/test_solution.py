from unittest import TestCase

from challenge_2_2_power_hungry import solution


class SolutionTestCase(TestCase):
    def test_solution(self):
        test_cases = [
            ([2, 0, 2, 2, 0], '8'),
            ([-2, -3, 4, -5], '60')
        ]

        for xs, expected in test_cases:
            self.assertEqual(expected, solution.solution(xs=xs))
