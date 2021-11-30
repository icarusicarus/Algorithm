num_words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def words_to_num(t):
    num = ""
    tmp = ""
    while t:
        tmp += t[0]
        t = t[1:]
        for nw in num_words:
            if nw in tmp:
                num += nums[num_words.index(nw)]
                tmp = ""

    return num


def solution(s):
    answer = ""
    if s.isdigit():
        answer = s
        return int(answer)

    tmp = ""
    for i in s:
        if (i.isdigit()) and (tmp == ""):
            answer += i
        elif (i.isdigit()) and (tmp != ""):
            answer += words_to_num(tmp)
            tmp = ""
            answer += i
        else:
            tmp += i
    answer += words_to_num(tmp)

    return int(answer)


if __name__ == "__main__":
    s = input()
    print(solution(s))
