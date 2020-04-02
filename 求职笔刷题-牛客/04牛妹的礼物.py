'''
题目描述
众所周知，牛妹有很多很多粉丝，粉丝送了很多很多礼物给牛妹，牛妹的礼物摆满了地板。
地板是N\times MN×M的格子，每个格子有且只有一个礼物，牛妹已知每个礼物的体积。
地板的坐标是左上角(1,1)  右下角（N, M）。
牛妹只想要从屋子左上角走到右下角，每次走一步，每步只能向下走一步或者向右走一步或者向右下走一步
每次走过一个格子，拿起（并且必须拿上）这个格子上的礼物。
牛妹想知道，她能走到最后拿起的所有礼物体积最小和是多少？

示例1
输入
[[1,2,3],[2,3,4]]

输出
7

说明
(1,1)->(1,2)->(2,3)

备注:
0<N,M<300
每个礼物的体积小于100
'''

#
# 
# @param presentVolumn int整型二维数组 N*M的矩阵，每个元素是这个地板砖上的礼物体积
# @return int整型
#
class Solution:
    def min3(self,a,b,c):
        return min(min(a,b),c)

    def selectPresent(self, presentVolumn):
        # write code here
        n = len(presentVolumn)
        if (n==0):
            return 0
        m = len(presentVolumn[1])
        for i in range(1,m):
            presentVolumn[0][i] += presentVolumn[0][i-1]
        for i in range(1,n):
            presentVolumn[i][0] += presentVolumn[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                presentVolumn[i][j] += self.min3(presentVolumn[i-1][j],presentVolumn[i][j-1],presentVolumn[i-1][j-1])
        return presentVolumn[n-1][m-1]
