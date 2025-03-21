def solution(info, n, m):
    ckpt = set([(0,0)])
    for x, y in info:
        n_ckpt = set()
        
        for xx, yy in ckpt:
            if xx + x < n:
                n_ckpt.add((xx+x,yy))
            if yy + y < m:
                n_ckpt.add((xx,yy+y))
        
        if n_ckpt:
            ckpt = n_ckpt
        else:
            return -1
        
    return min(A for A, _ in ckpt)


solution([[1, 2], [2, 3], [2, 1]],4,4)