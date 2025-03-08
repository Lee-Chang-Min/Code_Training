
k = 4  # 말의 개수

# 0은 흰색, 1은 빨간색, 2는 파란색
chess = [
    [0, 0, 2, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 2],
    [0, 2, 0, 0]
]

# 0,1,2,3
#오,왼, 위,아래
start_horse = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]


dr = [0,0,-1,1]
dc = [1,-1,0,0]


# 아 이거 쌓인 순서를 지정 해야함 -> 맵에서 어떻게 체스 말들이 쌓여져 있는지 저장해야 됨
# 쌓인 순서대로 같이 이동 -> stack
# 턴 한번은 1번 말부터 K번 말까지 순서대로 이동 -> 반복문을 통해 각 말을 이동 시키는 것이 필요

#말의 현재 위치
current = [
    [[0],[1],[2],0],
    [0,0,0,0],
    [0,0,[3],0],
    [0,0,0,0]
]


def getgameover (horse_count, game_map, horse_loc):
    n = len(game_map)
    print("n =",n)

    current = [[[] for _ in range(n)] for _ in range(n)]
    print(current)

    return


print(getgameover(k,chess,start_horse))




###############################
# n = 3
# [[[] for _ in range(n)] for _ in range(n)]
