import fractions
import functools
import itertools
from fractions import Fraction


def _take(iterable, length):
    return itertools.islice(iterable, length)


def _skip(iterable, length):
    return itertools.islice(iterable, length, None)


def solve_system_of_linear_equations(system):
    """
    https://en.wikipedia.org/wiki/Gaussian_elimination.
    """

    for column, pivot_row in _take(enumerate(system), len(system) - 1):
        pivot = pivot_row[column]

        for row in _skip(system, column + 1):
            scale = row[column] / pivot

            for i, pivot_i in _skip(enumerate(pivot_row), column + 1):
                row[i] -= pivot_i * scale

    for column, pivot_row in reversed(list(_skip(enumerate(system), 1))):
        pivot = pivot_row[column]

        for row in _take(system, column):
            scale = row[column] / pivot
            row[-1] -= pivot_row[-1] * scale

    return [row[-1] / row[i] for i, row in enumerate(system)]


def make_systems_of_linear_equations(matrix):
    non_terminal_states = []
    terminal_states = []
    probabilities = {}

    for i, row in enumerate(matrix):
        row_sum = sum(row)

        if row_sum == 0:
            terminal_states.append(i)
        else:
            non_terminal_states.append(i)
            probabilities[i] = [Fraction(num, row_sum) for num in row]

    systems = []

    for target_state in terminal_states:
        system = []

        for source_state in non_terminal_states:
            probabilities_row = probabilities[source_state]
            equation = []

            for next_state in non_terminal_states:
                if next_state == source_state:
                    equation.append(1 - probabilities_row[next_state])
                else:
                    equation.append(-probabilities_row[next_state])

            equation.append(probabilities_row[target_state])
            system.append(equation)

        systems.append(system)

    return systems


def solution(m):
    if all(num == 0 for num in m[0]):
        result = [1]

        for row in _skip(m, 1):
            if all(num == 0 for num in row):
                result.append(0)

        result.append(1)
    else:
        systems = make_systems_of_linear_equations(m)
        probabilities = [solve_system_of_linear_equations(system)[0] for system in systems]

        denominator = functools.reduce(lambda state, num: state * num // fractions.gcd(state, num),
                                       (probability.denominator for probability in probabilities))

        result = [(probability * denominator).numerator for probability in probabilities]

        result.append(denominator)

    return result
