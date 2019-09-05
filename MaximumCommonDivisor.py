# 欧几里德定理求2个数的最大公约数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mgcd(s):
    # 两两求最大公约数，会得到1个数组，在这个数组里再两两求公约数，如此递归，最终会得到1个只有1个数的数组，就是最大公约数
    if len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return gcd(s[0], s[1])
    else:
        cd = []
        for i in s:
            # 不求自己与自己的最大公约数
            if i != s[0]:
                cd.append(gcd(s[0], i))
        # 去除数组中的重复数据
        cd = list(set(cd))
        return mgcd(cd)


def greatest_common_divisor(*args):
    """
        Find the greatest common divisor
    """
    # 两两求最大公约数，会得到1个数组，在这个数组里再两两求公约数，如此递归，最终会得到1个只有1个数的数组，就是最大公约数
    return mgcd(args)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(greatest_common_divisor(3, 4))
    print(greatest_common_divisor(3, 4, 5))
    print(greatest_common_divisor(3, 4, 5, 6))
    print(greatest_common_divisor(3, 4, 5, 6, 7))