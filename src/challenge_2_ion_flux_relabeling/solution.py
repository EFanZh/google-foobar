def solve_one(num):
    tree_height = num.bit_length()
    root = (1 << tree_height) - 1

    if num == root:
        return num * 2 + 1
    elif num + 1 == root:
        return root
    else:
        subtree_size = (1 << (tree_height - 1)) - 1

        return solve_one(num - subtree_size) + subtree_size


def solution(h, q):
    root = (1 << h) - 1

    return [solve_one(num) if num < root else -1 for num in q]
