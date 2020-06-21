from fractions import Fraction
from unittest import TestCase

from challenge_x_1_disorderly_escape import solution


class SolutionTestCase(TestCase):
    def test_symmetric_group_cycle_indices(self):
        # https://oeis.org/A000166.

        test_cases = [
            (1, {frozenset([(1, 1)]): 1}),
            (2, {frozenset([(1, 2)]): Fraction(1, 2),
                 frozenset([(2, 1)]): Fraction(1, 2)}),
            (3, {frozenset([(1, 3)]): Fraction(1, 6),
                 frozenset([(1, 1), (2, 1)]): Fraction(1, 2),
                 frozenset([(3, 1)]): Fraction(1, 3)}),
        ]

        for n, expected in test_cases:
            self.assertEqual(expected, solution.symmetric_group_cycle_indices(n)[-1])

    def test_solution(self):
        test_cases = [
            ((2, 2, 2), '7'),
            ((2, 3, 1), '1'),
            ((2, 3, 2), '13'),
            ((2, 3, 3), '92'),
            ((2, 3, 4), '430'),
            ((2, 3, 5), '1505'),
            ((2, 3, 6), '4291')
        ]

        for (w, h, s), expected in test_cases:
            self.assertEqual(expected, solution.solution(w=w, h=h, s=s))
