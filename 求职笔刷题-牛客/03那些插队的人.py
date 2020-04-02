'''
题目背景：

随着社会整体素质的提高，插队的现象已经越来越少了。但是仍旧有一个特殊情况，需要对于某些人进行优先处理。当这些人完成了自己插队的壮举之后，
队伍的形态就变得千变万化。这个时候，得知每个人在哪里就变得尤为重要的，聪明的你一定可以完成这个艰巨的任务的，加油吧！

简明题意：

你有一个长度为 n 的队伍，从左到右依次为 1~n，有 m 次插队行为，用数组 cutIn 进行表示，cutIn 的元素依次代表想要插队的人的编号，每次插队，
这个人都会直接移动到队伍的最前方。你需要返回一个整数，代表这 m 次插队行为之后，有多少个人已经不在原来队伍的位置了。

示例1
输入
3,[3, 2, 3]
输出
2

说明
初始队伍为 [1, 2, 3]
3 开始插队 [3, 1, 2]
2 开始插队 [2, 3, 1]
3 开始插队 [3, 2, 1]
所以2还在原来的尾置，3和1两个人已经不在原来的位置了。

示例2
输入
3,[]
输出
0

说明
没有人进行插队，所有人都在自己原来的位置上。
备注:
对于所有数据，保证 n≤1e9, m≤1e4，且cutIn[i]≤n

分析：
15 [10,4,6,5,9,7,3,3,9,10] 
1.cutIn最大数之后的位置没有变。
2.cutIn列表中，没出现的数，且小于cutIn最大值，它的位置一定改变了。
myset()后插法。cutIn[i]后面又移动了cutIn[i]次，且没有再次插队，则它的位置没变。
'''

class Solution:
    def countDislocation(self , n , cutIn ):
        # write code here
        if len(cutIn) == 0:
            return 0
        else:
            len_ = len(cutIn)
            ma = max(cutIn)
            result = ma
            myset = set()
            for i in reversed(range(len_)):
                if not myset.__contains__(cutIn[i]) and len(myset)+1 == cutIn[i]:
                    result-=1
                myset.add(cutIn[i])
        return result
