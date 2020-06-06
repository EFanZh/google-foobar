import math


def _get_max_steps(bricks):
    return (int(math.sqrt(8 * bricks + 1)) - 1) // 2


def _get_max_min_height(bricks, steps):
    return (2 * bricks - steps * (steps - 1)) // (2 * steps)


def solution(n):
    result = 0
    previous_step_cache = [1] * (n + 1)
    current_step_cache = [0] * (n + 1)

    for steps in range(2, _get_max_steps(n) + 1):
        for bricks in range(steps * (steps + 1) // 2, n + 1):
            choices = 0

            for min_height in range(1, _get_max_min_height(bricks, steps) + 1):
                choices += previous_step_cache[bricks - min_height * steps]

            current_step_cache[bricks] = choices

        result += current_step_cache[-1]

        previous_step_cache, current_step_cache = current_step_cache, previous_step_cache

    return result
