r = 4
c = 4


def findmatch(mat, pat, x, y,
              nrow, ncol, level):
    l = len(pat)
    if (level == l):
        return True
    if (x < 0 or y < 0 or
            x >= nrow or y >= ncol):
        return False
    if (mat[x][y] == pat[level]):
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")
        res = (findmatch(mat, pat, x - 1, y, nrow, ncol, level + 1) |
               findmatch(mat, pat, x + 1, y, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y + 1, nrow, ncol, level + 1))

        mat[x].replace(mat[x][y], temp)
        return res
    else:
        return False


def checkMatch(mat, pat, nrow, ncol):
    l = len(pat)
    if (l > nrow * ncol):
        return False
    for i in range(nrow):
        for j in range(ncol):
            if (mat[i][j] == pat[0]):
                if (findmatch(mat, pat, i, j,
                              nrow, ncol, 0)):
                    return True
    return False


# Driver Code
if __name__ == "__main__":

    grid = ["CAT", "IDO",
            "NOM"]
    if (checkMatch(grid, "TOM", r, c)):
        print("Yes")
    else:
        print("No")
