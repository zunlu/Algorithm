'''
牛牛有两个长度为nn的数组a, ba,b，牛牛希望统计有多少数对(l, r)(l,r)满足：
1.0<=l<=r<=n-1
2.al+...ar=bl+br

示例1
输入
[1,2,3,4],[2,1,4,5]
输出
4

说明
满足条件的数对有(0, 1), (0, 2), (1, 1), (1, 2)(0,1),(0,2),(1,1),(1,2)
示例2
输入
[0,0,1,1,1],[2,0,4,3,3]
输出
2
'''


class Solution:
    def countLR( self,a , b ):
        total = 0
        suma=[0]*len(a)
        suma[0]=a[0]
        for i in range(1,len(a)):
            suma[i] = suma[i-1]+a[i]
        for i in range(len(a)):
            for j in range(i,len(a)):
                if(suma[j]-suma[i]+a[i] == b[i]+b[j]):
                    total +=1
        return total
