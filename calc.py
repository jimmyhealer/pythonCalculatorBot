def calc(array, N):
    list_x = []
    list_x.extend([x[0] for x in array])
    list_x.extend([x[2] for x in array])
    list_x = sorted(list(set(list_x)))
    list_y = []
    list_y.extend([x[1] for x in array])
    list_y.extend([x[3] for x in array])
    list_y = sorted(list(set(list_y)))
    numx, numy=len(list_x),len(list_y)

    mp = [[0 for i in range(numy-1)] for j in range(numx-1)]
    for i in range(N):
        L_x, R_x = list_x.index(array[i][0]), list_x.index(array[i][2])
        L_y, R_y = list_y.index(array[i][1]), list_y.index(array[i][3])
        for m in range(L_x,R_x):
            for n in range(L_y,R_y):
                mp[m][n]+=1
    area = 0
    for i in range(numx-1):
        for j in range(numy-1):
            if mp[i][j]:
                area += (list_x[i+1]-list_x[i])*(list_y[j+1]-list_y[j])
    return area