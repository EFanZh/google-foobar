from unittest import TestCase
from challenge_1_minion_labor_shifts import solution


class SolutionTestCase(TestCase):
    def test_solution(self):
        test_cases = [
            (([1, 2, 3], 0), []),
            (([1, 2, 2, 3, 3, 3, 4, 5, 5], 1), [1, 4])
        ]

        for (data, n), expected in test_cases:
            self.assertEqual(solution.solution(data=data, n=n), expected)
