# Examples
# Input: "onezeropluseight"
# Output: oneeight
# Input: "oneminusoneone"
# Output: negativeonezero


def StringChallenge(strParam):
    nums = [
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
        "plus",
        "minus",
    ]

    parsed = []
    tmp_str = ""
    idx = 0
    while len(strParam) != idx:
        tmp_str += strParam[idx]
        for i in range(len(nums)):
            if nums[i] in tmp_str:
                parsed.append(i)
                tmp_str = ""
        idx += 1

    last_op = 0
    fisrt_flag = 0
    tmp_str = ""
    num = 0
    for i in parsed:
        if i == 10:  # plus
            last_op = 0
            if fisrt_flag == 0:
                num += int(tmp_str)
                tmp_str = ""
                fisrt_flag == 1
            else:
                num += int(tmp_str)
                tmp_str = ""
        elif i == 11:  # minus
            last_op = 1
            if fisrt_flag == 0:
                num += int(tmp_str)
                tmp_str = ""
                fisrt_flag == 1
            else:
                num -= int(tmp_str)
                tmp_str = ""
        else:
            tmp_str += str(i)
        # print(i, tmp_str, num)

    if last_op == 0:
        num += int(tmp_str)
    else:
        num -= int(tmp_str)
    # print(num)

    if num < 0:
        result = "negative"
        num = abs(num)
    else:
        result = ""
    for i in str(num):
        result += nums[int(i)]

    # print(result)

    return result


print(StringChallenge(input()))
