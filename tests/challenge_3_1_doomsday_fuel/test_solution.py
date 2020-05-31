from fractions import Fraction
from unittest import TestCase

from challenge_3_1_doomsday_fuel import solution


class SolutionTestCase(TestCase):
    def test_solve_system_of_linear_equations(self):
        test_cases = [
            ([[2, 1, -1, 8],
              [-3, -1, 2, -11],
              [-2, 1, 2, -3]],
             [2, 3, -1]),
            ([[1, 2, 0, 3],
              [3, 4, 4, 7],
              [5, 6, 3, 8]],
             [Fraction(-7, 5), Fraction(11, 5), Fraction(3, 5)])
        ]

        for system, expected in test_cases:
            self.assertEqual(
                expected,
                solution.solve_system_of_linear_equations([[Fraction(num) for num in row] for row in system])
            )

    def test_make_systems_of_linear_equations(self):
        test_cases = [
            ([[0, 1, 0, 0, 0, 1],
              [4, 0, 0, 3, 2, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [[[1, Fraction(-1, 2), 0],
               [Fraction(-4, 9), 1, 0]],
              [[1, Fraction(-1, 2), 0],
               [Fraction(-4, 9), 1, Fraction(1, 3)]],
              [[1, Fraction(-1, 2), 0],
               [Fraction(-4, 9), 1, Fraction(2, 9)]],
              [[1, Fraction(-1, 2), Fraction(1, 2)],
               [Fraction(-4, 9), 1, 0]]]),
            ([[1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1]],
             [[[Fraction(4, 5), Fraction(-1, 5), Fraction(-1, 5), Fraction(1, 5)],
               [Fraction(-1, 5), Fraction(4, 5), Fraction(-1, 5), Fraction(1, 5)],
               [Fraction(-1, 5), Fraction(-1, 5), Fraction(4, 5), Fraction(1, 5)]],
              [[Fraction(4, 5), Fraction(-1, 5), Fraction(-1, 5), Fraction(1, 5)],
               [Fraction(-1, 5), Fraction(4, 5), Fraction(-1, 5), Fraction(1, 5)],
               [Fraction(-1, 5), Fraction(-1, 5), Fraction(4, 5), Fraction(1, 5)]]])
        ]

        for system, expected in test_cases:
            self.assertEqual(
                expected,
                solution.make_systems_of_linear_equations([[Fraction(num) for num in row] for row in system])
            )

    def test_solution(self):
        test_cases = [
            ([[0, 2, 1, 0, 0],
              [0, 0, 0, 3, 4],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]],
             [7, 6, 8, 21]),
            ([[0, 1, 0, 0, 0, 1],
              [4, 0, 0, 3, 2, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [0, 3, 2, 9, 14]),
            ([[0]],
             [1, 1]),
            ([[0, 0, 0],
              [0, 1, 2],
              [0, 0, 0]],
             [1, 0, 1]),
            ([[1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1]],
             [1, 1, 2])
        ]

        for m, expected in test_cases:
            self.assertEqual(expected, solution.solution(m=m))
