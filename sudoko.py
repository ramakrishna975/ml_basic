def check(i, j, x, s):
    a = (i // 3) * 3
    c = (j // 3) * 3
    for k in range(a, a + 2):
        for h in range(c, c + 2):
            if x == s[k][h] and (k != i and h != j):
                return 0

    for k in range(9):
        if s[i][k] == x and j != k:
            return 0
        if s[k][j] == x and i != k:
            return 0
    return 1


s=[[0,5,2,0,0,6,0,0,0],
   [1,6,0,9,0,0,0,0,4],
   [0,4,9,8,0,3,6,2,0],
   [4,0,0,0,0,0,8,0,0],
   [0,8,3,2,0,1,5,9,0],
   [0,0,1,0,0,0,0,0,2],
   [0,9,7,3,0,5,2,4,0],
   [2,0,0,0,0,9,0,5,6],
   [0,0,0,1,0,0,9,7,0]]

while (1):
    for i in range(9):
        for j in range(9):
            count = 0
            if s[i][j] == 0:
                for x in range(1, 10):
                    if check(i, j, x, s):
                        count = count + 1
                        y = x
                if count == 1:
                    s[i][j] = y

            ch = 0
            for k in range(9):
                for l in range(9):
                    if s[k][l] != 0:
                        ch += 1

            if ch == 81:
                for l in s:
                    print(l)
                exit()