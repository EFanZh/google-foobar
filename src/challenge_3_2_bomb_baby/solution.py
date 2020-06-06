def solution(x, y):
    x = int(x)
    y = int(y)

    if y < x:
        x, y = y, x

    result = 0

    while x != 0:
        result += y // x
        x, y = y % x, x

    return str(result - 1) if y == 1 else 'impossible'
