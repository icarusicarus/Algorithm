ropes = []


def solution():
    # max_weight = min(ropes)
    # return max_weight * len(ropes)
    max_weight = 0
    ropes.sort()
    while len(ropes) != 0:
        weight = ropes[0] * len(ropes)
        ropes.remove(ropes[0])
        if weight > max_weight:
            max_weight = weight

    return max_weight


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        ropes.append(int(input()))

    print(solution())
