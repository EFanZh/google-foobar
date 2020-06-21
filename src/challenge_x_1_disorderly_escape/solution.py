import fractions
from fractions import Fraction


def symmetric_group_cycle_indices(n):
    """
    https://en.wikipedia.org/wiki/Cycle_index#Symmetric_group_Sn.
    """

    results = [{frozenset([(1, 1)]): 1}]

    for i in range(2, n + 1):
        result = {}

        for j in range(1, i):
            for key, value in results[i - j - 1].items():
                key_2 = dict(key)

                try:
                    key_2[j] += 1
                except KeyError:
                    key_2[j] = 1

                key_2 = frozenset(key_2.items())

                try:
                    result[key_2] = result.pop(key_2) + Fraction(value, i)
                except KeyError:
                    result[key_2] = Fraction(value, i)

        result[frozenset([(i, 1)])] = Fraction(1, i)

        results.append(result)

    return results


def solution(w, h, s):
    """
    https://math.stackexchange.com/questions/2113657/burnsides-lemma-applied-to-grids-with-interchanging-rows-and-columns.
    """

    result = 0
    cycle_indices = symmetric_group_cycle_indices(max(w, h))

    for row_key, row_value in cycle_indices[h - 1].items():
        for column_key, column_value in cycle_indices[w - 1].items():
            cycle_count = 0

            for row_cycle_length, row_cycle_count in row_key:
                for column_cycle_length, column_cycle_count in column_key:
                    count = row_cycle_count * column_cycle_count
                    cycle_count += fractions.gcd(row_cycle_length, column_cycle_length) * count

            result += (row_value * column_value) * (s ** cycle_count)

    return str(result)
