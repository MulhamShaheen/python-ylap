import itertools
import math


def domain_name(url):
    if "www" in url:
        return url.split(".")[1]

    url = url.split("//")[1]
    return url.split(".")[0]


def int32_to_ip(int32):
    ip = ""
    i = 3
    while i > 0:
        temp = int32 // 256 ** i
        ip += str(temp) + "."

        int32 = int32 % 256 ** i
        i -= 1

    ip += str(int32)
    return ip


def zeros(n):
    count_fives = n // 5
    count_twos = n // 2

    count_twos -= count_fives
    count = count_fives + (count_twos // 5)
    return count


def bananas(s):
    result = set()
    banana = "banana"
    iterable = [x for x in [1] * 6] + [x for x in [0] * (len(s) - 6)]

    temp = []
    for i in itertools.permutations(iterable, len(s)):
        if i.count(1) == 6:
            word = ""
            for j in range(len(s)):
                if i[j]:
                    word += s[j]
                else:
                    word += "-"

            temp.append(word)

    for i in temp:
        if i.replace("-", "") == banana:
            result.add(i)

    return result


def count_find_num(primesL, limit):
    minimum = 1
    maximum = minimum

    for i in primesL:
        minimum *= i
    temp = minimum

    if temp > limit:
        return []

    n = int(math.log(limit - minimum, min(primesL)))
    iter = itertools.combinations_with_replacement(primesL + [1], n - len(primesL))
    count = 0
    for i in iter:
        temp = minimum
        for j in i:
            temp *= j
        if minimum <= temp <= limit:
            if temp > maximum:
                maximum = temp
            count += 1

    return [count, maximum]


