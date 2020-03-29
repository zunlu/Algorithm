
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
