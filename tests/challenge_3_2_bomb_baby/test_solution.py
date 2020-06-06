from unittest import TestCase

from challenge_3_2_bomb_baby import solution


class SolutionTestCase(TestCase):
    def test_solution(self):
        test_cases = [
            (('4', '7'), '4'),
            (('2', '1'), '1'),
            (('2', '4'), 'impossible')
        ]

        for (x, y), expected in test_cases:
            self.assertEqual(expected, solution.solution(x=x, y=y))
