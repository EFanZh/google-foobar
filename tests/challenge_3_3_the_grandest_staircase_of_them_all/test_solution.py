from unittest import TestCase

from challenge_3_3_the_grandest_staircase_of_them_all import solution


class SolutionTestCase(TestCase):
    def test_solution(self):
        test_cases = [
            (3, 1),
            (4, 1),
            (5, 2),
            (6, 3),
            (7, 4),
            (8, 5),
            (9, 7),
            (10, 9),
            (11, 11),
            (12, 14),
            (13, 17),
            (14, 21),
            (15, 26),
            (16, 31),
            (40, 1112),
            (73, 40025),
            (100, 444792),
            (200, 487067745)
        ]

        for n, expected in test_cases:
            self.assertEqual(expected, solution.solution(n=n))
