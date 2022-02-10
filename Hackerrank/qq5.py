#!/bin/python3

import sys

# input
# 12
# push 4
# pop
# push 3
# push 5
# push 2
# inc 3 1
# pop
# push 1
# inc 2 2
# push 4
# pop
# pop

# 8
# push -36
# push 20
# pop
# push -9
# pop
# push -53
# pop
# inc 1 -17

# 10
# push 15
# pop
# push -51
# pop
# push 41
# pop
# push -76
# push 51
# push -10
# inc 1 -49

# output
# 4
# EMPTY
# 3
# 5
# 2
# 3
# 6
# 1
# 1
# 4
# 1
# 8

# -36
# 20
# -36
# -9
# -36
# -53
# -36
# -53

# 15
# EMPTY
# -51
# EMPTY
# 41
# EMPTY
# -76
# 51
# -10
# -10

# Complete the function below.


def superStack(operations):
    stack = []
    # result = []

    for op in operations:
        if op[:4] == "push":
            stack.append(int(op.split(" ")[1]))
            # result.append(stack[-1])
            print(stack[-1])

        elif op[:3] == "pop":
            stack.remove(stack[-1])
            if len(stack) != 0:
                # result.append(stack[-1])
                print(stack[-1])
            else:
                # result.append('EMPTY')
                print("EMPTY")

        else:  # inc
            add_range = int(op.split(" ")[1])
            add_value = int(op.split(" ")[2])

            for i in range(add_range):
                stack[i] += add_value
            # result.append(stack[-1])
            print(stack[-1])

    return 0


if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    operations = []
    while operations_i < operations_cnt:
        try:
            operations_item = str(input())
        except:
            operations_item = None
        operations.append(operations_item)
        operations_i += 1

    res = superStack(operations)
