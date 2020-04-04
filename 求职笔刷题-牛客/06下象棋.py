'''
下象棋
时间限制 :1sec / 空间限制: 256MB

题意：
牛妹在和牛牛下牛客象棋。现在轮到牛妹了，牛妹想知道她在这一回合能否战胜牛牛。

棋盘chessboard上只可能包含：炮，将，车，兵

牛客象棋的规则解释：
炮：炮在不吃子的时候，走动与车完全相同，但炮在吃棋子时，必须跳过一个棋子，我方的和敌方的都可以
兵：可以上下左右移动，每次只能移动一格
车：上下左右均可走，只要无棋子阻拦，步数不受限制。
将：可以上下左右移动，每次只能移动一格
接下来给出一个棋盘，牛妹的棋子用大写字母表示，牛牛的棋子用小写字母表示。
将用J,jJ,j表示，炮用P,pP,p表示，车用C,cC,c表示，兵用B,bB,b表示，没有棋子的格子用..表示
保证棋盘上一定同时包含JJ与jj各一个。

输入：

给定chessboard数组
6≤chessboard.size≤10^3
6≤chessboard[i].length≤10^3

 


输出：
牛妹能胜利则返回"Happy"，否则返回"Sad"

示例1

输入
["......", "..B...", "P.C.j.", "......", "..b..."," ...J.." ]
输出
"Happy"
说明
牛妹的炮可以攻击到牛牛的将，所以获胜
'''


# @param chessboard string字符串一维数组
# @return string字符串
#
class Solution:
    def playchess(self , chessboard ):
        # write code here
        flag= 1
        temp = 0
        n = len(chessboard)
        m = len(chessboard[1])
        for i in range(n):
            for j in range(m):
                if(chessboard[i][j] == 'j'):
                    if((i and (chessboard[i-1][j] == 'B' or chessboard[i-1][j] == 'J')) or (i<m-1 and (chessboard[i+1][j] == 'B' or chessboard[i+1][j] == 'J')) or (j and (chessboard[i][j-1] == 'B' or chessboard[i][j-1] == 'J')) or (j<n-1 and (chessboard[i][j+1] == 'B' or chessboard[i][j+1] == 'J'))):
                        return "Happy"
                    #上
                    temp = i-1
                    while(temp>=0):
                         #这个条件花了很长时间才写对！！！
                        if(chessboard[temp][j] != '.' and chessboard[temp][j] !='P'  and chessboard[temp][j] != 'C'):
                            flag = 0
                        if((flag and (chessboard[temp][j] == 'C')) or ((not flag )and (chessboard[temp][j] == 'P'))):
                            return "Happy"
                        temp-=1
                    #下
                    temp = i+1
                    flag = 1
                    while (temp < n ):
                        if (chessboard[temp][j] != '.' and chessboard[temp][j] !='P' and chessboard[temp][j] != 'C'):
                            flag = 0
                        if ((flag and (chessboard[temp][j] == 'C')) or ((not flag) and (chessboard[temp][j] == 'P'))):
                            return "Happy"
                        temp += 1
                    #右
                    temp = j+1
                    flag = 1
                    while (temp < m ):
                        if (chessboard[i][temp] != '.' and chessboard[i][temp] != 'P' and chessboard[i][temp] != 'C'):
                            flag = 0
                        if ((flag and (chessboard[i][temp] == 'C')) or ((not flag) and (chessboard[i][temp] == 'P'))):
                            return "Happy"
                        temp += 1
                    #左
                    temp = j-1
                    flag = 1
                    while (temp >= 0 ):
                        if (chessboard[i][temp] !='.' and chessboard[i][temp] != 'P' and chessboard[i][temp] != 'C' ):
                            flag = 0
                        if ((flag and (chessboard[i][temp] == 'C')) or ((not flag) and (chessboard[i][temp] == 'P'))):
                            return "Happy"
                        temp -= 1
        return "Sad"
