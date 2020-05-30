from unittest import TestCase

from challenge_2_1_ion_flux_relabeling import solution


class SolutionTestCase(TestCase):
    def test_solve_one(self):
        test_cases = [
            (1, 3),
            (2, 3),
            (3, 7),
            (4, 6),
            (5, 6),
            (6, 7),
            (7, 15),
            (8, 10),
            (9, 10)
        ]

        for num, expected in test_cases:
            self.assertEqual(expected, solution.solve_one(num=num))

    def test_solution(self):
        test_cases = [
            ((3, [7, 3, 5, 1]), [-1, 7, 6, 3]),
            ((5, [19, 14, 28]), [21, 15, 29])
        ]

        for (h, q), expected in test_cases:
            self.assertEqual(expected, solution.solution(h=h, q=q))
