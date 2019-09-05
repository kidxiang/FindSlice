import math

"""
    获得多个数的最小公倍数
    isPrime(n)
    getMutiPrime(n)
    getLeastCommonMutible(numList)
"""


def isPrime(n):
    """
    判断一个数是否是质数
    """
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    p = int(math.sqrt(n)) + 1
    i = 3
    while i < p:
        if n % i == 0:
            return False
        i += 2
    return True


def getMutiPrime(n):
    """get muti num of n
    n=num1*num2...*numx for num1...numx are all prime numbers
    将数n进行质因数分解 prime factorization
    """
    if n == 2:
        resultlist = [2]
    else:
        list1 = [i for i in range(2, int(math.sqrt(n)) + 1) if isPrime(i)]
        # print(list1)
        resultlist = []
        tmp = n
        while not isPrime(tmp) and tmp != 1:
            for i in list1:
                if tmp % i == 0:
                    resultlist.append(i)
                    tmp = tmp // i
                    # print(tmp)
                    # print(resultlist)
        if tmp != 1:
            resultlist.append(tmp)
    return resultlist


def isMutillistFill(mutilLsit):
    """
    	判断一个二维列表中的每一个列表是否都为空
    	mutilLsit=[[],[],[]] 返回False
    	mutilLsit=[[1],[],[]] 返回True
    """
    for row in mutilLsit:
        if len(row) > 0:
            return True
    return False


def getLeastCommonMutible(numList):
    """
    numList 待求数的列表，
    返回它们的最小公倍数的质因数列表
    """
    primelists = []
    set1 = set({})
    mutilResult = []
    for i in numList:
        primelists.append(getMutiPrime(i))
        set1.update(set(i1 for i1 in getMutiPrime(i)))
    # print(primelists)
    flag = True
    flag1 = False
    while flag:
        for i in set1:
            for row in primelists:
                if i in row:
                    row.remove(i)
                    flag1 = True
            if flag1:
                mutilResult.append(i)
                flag1 = False
        flag = isMutillistFill(primelists)
    # print(mutilResult)
    return mutilResult


def getMutil(numList):
    result = 1
    for i in numList:
        result *= i
    return result

def getLCM(numList):
        return getMutil(getLeastCommonMutible(numList))

if __name__ == '__main__':
    print(getLCM([3, 4, 5]))# 获取8,12,20的最小公倍数
    print(getLCM([i for i in range(2, 21)]))  # 获取1到20的所有数的最小公倍数