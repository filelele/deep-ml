def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b): 
        return -1
    
    nrow_res = len(a)
    ncol_res = len(b[0])
    res = []

    for row in range(nrow_res):
        row_i_res = []
        row_a = a[row]
        for col in range(ncol_res):
            col_b = []
            for row_b in range(len(b)):
                col_b.append(b[row_b][col])
            row_i_res.append(sum([x*y for x,y in zip(row_a, col_b)]))
        res.append(row_i_res)
	
    return res