def isqrt(x):
    i = x

    while i * i > x:
        i = (i + x // i) // 2

    return i


def solution_helper_2(s):
    """
    Returns `sum(floor((2 + sqrt(2)) * i) for i in range(1, s + 1))`.
    """

    return 0 if s == 0 else solution_helper_1(s) + s * (s + 1)


def solution_helper_1(s):
    """
    Returns `sum(floor(sqrt(2) * i) for i in range(1, s + 1))`.
    """

    last = isqrt(2 * s * s)
    s_2 = last - (isqrt(2 * last * last) + 2) // 2

    return last * (last + 1) // 2 - solution_helper_2(s_2)


def solution(s):
    """
    https://en.wikipedia.org/wiki/Beatty_sequence.
    """

    return str(solution_helper_1(int(s)))
