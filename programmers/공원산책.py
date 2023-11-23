def solution(park, routes):
    arr = []
    x, y= 0, 0
    H, W = len(park), len(park[0])
        
    for i in range(H):
        arr.append(list(map(str, park[i])))
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'S':
                x, y = i, j
    
    for item in routes:
        dir, dist = item.split()
        dist = int(dist)
        nx = x
        ny = y
        for _ in range(dist):
            if dir == "E": 
                ny += 1
            if dir == "S": 
                nx += 1
            if dir == "W": 
                ny -= 1
            if dir == "N": 
                nx -= 1
            if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] == "X": break
        if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != "X":
            x = nx
            y = ny
                    
    answer = [x, y]
    return answer