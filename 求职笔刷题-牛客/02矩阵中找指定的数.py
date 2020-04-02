‘’‘
题目描述
给定一个N \times MN×M的整形矩阵matrix和一个整数K, matrix的每一行和每一列都是排好序的。
实现一个函数，判断K是否在matrix中
[要求]
时间复杂度为O(N+M)O(N+M)，额外空间复杂度为O(1)O(1)。
输入描述:
第一行有三个整数N, M, K
接下来N行，每行M个整数为输入的矩阵
输出描述:
若K存在于矩阵中输出"Yes"，否则输出"No"
示例1
输入
复制
2 4 5
1 2 3 4
2 4 5 6
输出
复制
Yes
示例2
输入
复制
2 4 233
1 2 3 4
2 4 5 6
输出
复制
No
备注:
1 \leqslant N, M \leqslant 10001⩽N,M⩽1000
0 \leqslant K, \text{矩阵中的数} \leqslant 10^90⩽K,矩阵中的数⩽10 
9
 


’‘’
def isContains(mat, k):
    if len(mat) == 0 or len(mat[0]) == 0:
        return False
    row = 0
    col = len(mat[0]) - 1
    while row < len(mat) and col >= 0:
        if int(mat[row][col]) == k:
            return True
        elif int(mat[row][col]) < k:
            row += 1
        else:
            col -= 1
    return False
if __name__ =="__main__":
    n,m,k = map(int,input().split())
    mat = [[0]*m]*n
    for i in range(n):
        mat[i]=input().split(' ')
    # print(type(int(mat[1][1])))
    if(isContains(mat,k)):
        print('Yes')
    else:
        print('No')
