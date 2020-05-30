def solution(xs):
    iterator = iter(xs)
    min_product = next(iterator)
    max_product = min_product

    for power_output in iterator:
        if power_output < 0:
            new_min_product = min(min_product, max_product * power_output, power_output)
            new_max_product = max(max_product, min_product * power_output, power_output)
        elif power_output == 0:
            new_min_product = min(min_product, 0)
            new_max_product = max(max_product, 0)
        else:
            new_min_product = min(min_product, min_product * power_output, power_output)
            new_max_product = max(max_product, max_product * power_output, power_output)

        min_product = new_min_product
        max_product = new_max_product

    return str(max_product)
