def calc(array, N):
    list_x = []
    list_x.extend([x[0] for x in array])
    list_x.extend([x[2] for x in array])
    list_y = []
    list_y.extend([x[1] for x in array])
    list_y.extend([x[3] for x in array])
    maxX, maxY = max(list_x), max(list_y)
    minX, minY = min(list_x), min(list_y)
    mp = [[-1 for _ in range(maxY - minY + 1)] for __ in range(maxX - minX + 1)]
    for i in range(N):
        for m in range(array[i][0] - minX, array[i][2] - minX):
            for n in range(array[i][1] - minY, array[i][3] - minY):
                mp[m][n] = array[i][4]
    totArea = 0
    colorArea = [0 for _ in range(8)]

    for i in range(maxX - minX + 1):
        for j in range(maxY - minY + 1):
            if mp[i][j] != -1:
                totArea += 1
                colorArea[mp[i][j]] += 1
    
    return totArea, colorArea

    # for i in range(N):
    #     L_x, R_x = list_x.index(array[i][0]), list_x.index(array[i][2])
    #     L_y, R_y = list_y.index(array[i][1]), list_y.index(array[i][3])
    #     for m in range(L_x,R_x):
    #         for n in range(L_y,R_y):
    #             mp[m][n]+=1
    # area = 0
    # for i in range(numx-1):
    #     for j in range(numy-1):
    #         if mp[i][j]:
    #             area += (list_x[i+1]-list_x[i])*(list_y[j+1]-list_y[j])
    # return area