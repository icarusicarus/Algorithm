def count_case(s):
    num_a = 0
    for i in range(len(s)):
        if s[i] == "a":
            num_a += 1

    if (num_a % 3) != 0:
        return 0
    n = num_a / 3

    flag = 0
    idx_a = 0
    prev_idx_b = 0
    idx_b = 0
    for i in range(len(s)):
        if idx_a == n:
            idx_a = 0
        if s[i] == "a":
            if flag == 1:
                flag = 0
                prev_idx_b = idx_b
                idx_b = 0
            idx_a += 1
        if (s[i] == "b") and (idx_a == 0):
            flag = 1
            idx_b += 1
        print(s[i], idx_a, idx_b, prev_idx_b)

    return (prev_idx_b + 1) * (idx_b + 1)


if __name__ == "__main__":
    s = input()
    print(count_case(s))
