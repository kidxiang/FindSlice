import LeastCommonMultiple
from itertools import combinations

def findSlice(minSlice = 180, step=60, maxLCM = 43200):
    """计算分片组合

    :param minSlice:最小分片数
    :param step: 分片增量
    :param maxLCM: 最大的最小公倍数，超出这个数即停止运算————预期的在这个数值内保证分片不重复
    :return:
        1/0 : 1表示达到maxLCM退出得出的结果；0表示未达到maxLCM退出得到的结果，即完美结果
        subSliceList：得到的分片组合
        lcm：实际的最小公倍数，即实际的在这个数值内保证分片不重复
    """
    #初始化分片组合列表
    sliceList = []
    sliceList.append(minSlice)
    #初始化下一个分片数
    nextSlice = minSlice
    #初始化已经计算过的分片组合
    usedSliceList = []
    #初始化已经计算过的最小公倍数
    usedLCM = []

    while 1: #无线循环
        #按照分片增量增加下一个分片数
        nextSlice = nextSlice + step
        sliceList.append(nextSlice)
        #初始化组合长度
        i = 2
        while i < len(sliceList): # 当组合长度小于分片组合列表长度
            allSubSliceList = list(combinations(sliceList, i)) # 将分片列表按长度进行全量组合（排列组合中的组合）
            for subSliceList in allSubSliceList: # 遍历每一个分片组合
                if subSliceList not in usedSliceList and minSlice in subSliceList: #如果当前组合没有计算过 并且 最小分片数在当前分片组合中（为了提升程序效率）
                    lcm = LeastCommonMultiple.getLCM(subSliceList) #计算当前组合的最小公倍数
                    if lcm not in usedLCM: #如何当前组合的最小公倍数没有被计算过
                        numSuccess = False # 初始化完美计算成功为False
                        for num in range(lcm, minSlice - 1, -1): #从大到小遍历最小公倍数
                            numSuccess = False # 重置完美计算成功为False
                            for slice in reversed(subSliceList): #遍历每一个分片数
                                if slice / minSlice > 1 and slice % minSlice == 0: #如果当前分片数是最小分片数的倍数
                                    continue #跳过该分片数
                                remainder = num % slice #计算当前分片数的余数
                                if remainder == 0 or remainder >= minSlice: #如果能除仅 或者 余数大于最小分片数
                                    numSuccess = True #当前分片数满足需求，计算成功
                                    break #不用再计算其他分片数，退出变量分片数循环
                                else:
                                    numSuccess = False #当前分片数不满足需求，计算失败
                            if numSuccess == False: #如果每一个分片数都计算失败
                                break #当前分片组合计算失败，退出当前分片组合计算
                    usedLCM.append(lcm) #将当前组合的最小公倍数加入到已计算过的最小公倍数列表（为了提升程序效率）
                    if numSuccess == True: #当前分片组合的每一个分片数均计算成功，即完美计算
                        return 0, subSliceList, lcm #返回完美计算结果
                    else: #未完美计算成功
                        if lcm > maxLCM: #如果当前计算的最小公倍数已满足我们的最大的最小公倍数要求
                            return 1, subSliceList, lcm #返回非完美计算结果，但该结果已能满足要求
                    #print(subSliceList)
                usedSliceList.append(subSliceList) #将当前分片组合加入已计算过的分片组合列表
            i += 1 #组合长度加1

    return 2 #非正常退出

if __name__ == '__main__':
    print(findSlice()) # 找最小分片为3的分片组合

