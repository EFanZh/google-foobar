def solution(data, n):
    count = {}

    for num in data:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return [num for num in data if count[num] <= n]
