ID_MIN = 3
ID_MAX = 15


def solution(id):
    answer = ''
    # Step 1
    id = id.lower()

    # Step 2
    for c in id:
        a = ord(c)
        if (not ((48 <= a <= 57) or (97 <= a <= 122) or a == 45 or a == 46 or a == 95)):
            id = id.replace(c, "")

    # Step 3
    it = len(id) - 2
    i = 0
    while (it > 0):
        if (id[i] == '.'):
            j = 1

            if ((i+j) < (len(id) - 1)):
                while (id[i+j] == '.'):
                    j += 1
            else:
                it = 0
            id = id[0:i+1]+id[i+j:]
            it -= j
        i += 1
        it -= 1

    # Step 4
    if ((len(id) != 0) and (id[0] == '.')):
        id = id[1:]
    if ((len(id) != 0) and (id[-1] == '.')):
        id = id[:-2]

    # Step 5
    if (len(id) == 0):
        id = 'a'

    # Step 6
    if (len(id) > ID_MAX):
        id = id[:15]
        if (id[-1] == '.'):
            id = id[:-1]

    # Step 7
    if (len(id) < ID_MIN):
        while (len(id) < ID_MIN):
            append_char = id[-1]
            id = id + append_char
    answer = id
    return answer


if __name__ == '__main__':
    origin_id = input()
    print(solution(origin_id))
