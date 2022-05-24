import random
import pygame  # 1. pygame 선언
import copy

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
size = [800, 1000]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048 and Auto")



done = False
gameOver = False
clock = pygame.time.Clock()

mainscore = 0
simulScore = 0
minDepth = 0
maxSimul = 0
code = 0
minTwoandFour = 20



# 4. pygame 무한루프

#direc 0 = left, 1 = right 2 = up 3 = down
def move(map, direc, score, mode= False):
    success = False
    global mainscore
    global simulScore

    if direc == 0:
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[i][k-1] == 0 and map[i][k] !=0:
                        map[i][k-1] = map[i][k]
                        map[i][k] = 0
                        success = True

        for i in range(4):
            for j in range(1, 4):
                if map[i][j-1] == map[i][j] and map[i][j-1] != 0:
                    map[i][j - 1] += map[i][j]
                    map[i][j] = 0

                    score = score + map[i][j - 1]
                    if mode:
                        mainscore = score
                    else:
                        simulScore = score

                    success = True

        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[i][k-1] == 0 and map[i][k] !=0:
                        map[i][k - 1] = map[i][k]
                        map[i][k] = 0

    if direc == 1:
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[i][k+1] == 0 and map[i][k] != 0:
                        map[i][k+1] = map[i][k]
                        map[i][k] = 0
                        success = True

        for i in range(4):
            for j in range(3, 0, -1):
                if map[i][j-1] == map[i][j] and map[i][j] != 0:
                    map[i][j] += map[i][j - 1]
                    map[i][j - 1] = 0
                    success = True
                    score = score + map[i][j]
                    if mode:
                        mainscore = score
                    else :
                        simulScore = score


        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[i][k + 1] == 0 and map[i][k] != 0:
                        map[i][k + 1] = map[i][k]
                        map[i][k] = 0

    if direc == 2:
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[k-1][i] == 0 and map[k][i] != 0:
                        map[k-1][i] = map[k][i]
                        map[k][i] = 0
                        success = True

        for i in range(4):
            for j in range(1, 4):
                if map[j-1][i] == map[j][i] and map[j][i] != 0:
                    map[j - 1][i] += map[j][i]
                    map[j][i] = 0
                    success = True

                    score = score + map[j - 1][i]
                    if mode:
                        mainscore = score
                    else :
                        simulScore = score

        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[k-1][i] == 0 and map[k][i] != 0:
                        map[k - 1][i] = map[k][i]
                        map[k][i] = 0

    if direc == 3:
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[k+1][i] == 0 and map[k][i] != 0:
                        map[k + 1][i] = map[k][i]
                        map[k][i] = 0
                        success = True

        for i in range(4):
            for j in range(3, 0, -1):
                if map[j - 1][i] == map[j][i] and map[j][i] != 0:
                    map[j][i] += map[j - 1][i]
                    map[j - 1][i] = 0
                    success = True
                    score = score + map[j][i]
                    if mode:
                        mainscore = score
                    else :
                        simulScore = score

        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[k+1][i] == 0 and map[k][i] != 0:
                        map[k + 1][i] = map[k][i]
                        map[k][i] = 0

    return success



#direc 0 = left, 1 = right 2 = up 3 = down
def move2(map, direc, score, mode= False):
    success = False
    global mainscore
    global simulScore

    if direc == 0:
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[i][k-1] == 0 and map[i][k] !=0:
                        map[i][k-1] = map[i][k]
                        map[i][k] = 0
                        success = True

        for i in range(4):
            for j in range(1, 4):
                if map[i][j-1] == map[i][j] and map[i][j-1] != 0:
                    map[i][j - 1] += map[i][j]
                    map[i][j] = 0

                    simulScore = simulScore +1

                    success = True

        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[i][k-1] == 0 and map[i][k] !=0:
                        map[i][k - 1] = map[i][k]
                        map[i][k] = 0

    if direc == 1:
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[i][k+1] == 0 and map[i][k] != 0:
                        map[i][k+1] = map[i][k]
                        map[i][k] = 0
                        success = True

        for i in range(4):
            for j in range(3, 0, -1):
                if map[i][j-1] == map[i][j] and map[i][j] != 0:
                    map[i][j] += map[i][j - 1]
                    map[i][j - 1] = 0
                    success = True
                    simulScore = simulScore +1


        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[i][k + 1] == 0 and map[i][k] != 0:
                        map[i][k + 1] = map[i][k]
                        map[i][k] = 0

    if direc == 2:
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[k-1][i] == 0 and map[k][i] != 0:
                        map[k-1][i] = map[k][i]
                        map[k][i] = 0
                        success = True

        for i in range(4):
            for j in range(1, 4):
                if map[j-1][i] == map[j][i] and map[j][i] != 0:
                    map[j - 1][i] += map[j][i]
                    map[j][i] = 0
                    success = True

                    simulScore = simulScore +1
        for i in range(4):
            for j in range(1, 4):
                for k in range(j, 0, -1):
                    if map[k-1][i] == 0 and map[k][i] != 0:
                        map[k - 1][i] = map[k][i]
                        map[k][i] = 0

    if direc == 3:
        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[k+1][i] == 0 and map[k][i] != 0:
                        map[k + 1][i] = map[k][i]
                        map[k][i] = 0
                        success = True

        for i in range(4):
            for j in range(3, 0, -1):
                if map[j - 1][i] == map[j][i] and map[j][i] != 0:
                    map[j][i] += map[j - 1][i]
                    map[j - 1][i] = 0
                    success = True
                    simulScore = simulScore +1

        for i in range(4):
            for j in range(3, -1, -1):
                for k in range(j, 3):
                    if map[k+1][i] == 0 and map[k][i] != 0:
                        map[k + 1][i] = map[k][i]
                        map[k][i] = 0

    return success


#처음엔 시뮬레이션으로 최댓값이 오게 설정을 하게되었는데 depth에 따라 과 시뮬레이션으로 모두 동점을 받을 수있음
#그렇다고 depth 임계치를 낮추면 정확도가 적거나, 최적해를 반영하기 힘듬.
# 따라서 시뮬레이션에서 최댓값 + 그 최댓값의 최소 깊이를 반영해야 함.
# 첫 번째 시뮬레이션은 지금 당장 높은 점수를 얻는 방향으로 진행됨.  두번째 시뮬레이션은 빈칸을 늘리는 방향으로 진행할 예정

def simulation(list_map, depth, score, direc, orin):
    global simulScore, maxSimul, minDepth
    global code

    simulScore = score
    direcList =[0,1,2,3]
    random.shuffle(direcList)

    if depth == 8:
        return

    if direc != direcList[0]:
        if direc ==5:
            orin = direcList[0]
        newMap = copy.deepcopy(list_map)

        move(newMap, direcList[0], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation(newMap, depth + 1, simulScore, direcList[0], orin)

        simulScore = score

    if direc != direcList[1]:
        if direc ==5:
            orin = direcList[1]
        newMap = copy.deepcopy(list_map)
        move(newMap, direcList[1], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation(newMap, depth + 1, simulScore, direcList[1], orin)


        simulScore = score

    if direc != direcList[2]:
        if direc ==5:
            orin = direcList[2]
        newMap = copy.deepcopy(list_map)
        move(newMap, direcList[2], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation(newMap, depth + 1, simulScore, direcList[2], orin)
        simulScore = score

    if direc != direcList[3]:
        if direc ==5:
            orin = direcList[3]
        newMap = copy.deepcopy(list_map)
        move(newMap, direcList[3], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation(newMap, depth + 1, simulScore, direcList[3], orin)
        simulScore = score

    return code



#공평하게 갯수를 가장 많이 줄이는것에 초점을 둬본다.
def simulation2(list_map, depth, score, direc, orin):
    global simulScore, maxSimul, minDepth
    global code

    simulScore = score
    direcList =[0,1,2,3]
    random.shuffle(direcList)       #순서비교의 편향을 방지

    if depth == 8:
        return

    if direc != direcList[0]:
        if direc ==5:
            orin = direcList[0]
        newMap = copy.deepcopy(list_map)

        move2(newMap, direcList[0], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation2(newMap, depth + 1, simulScore, direcList[0], orin)

        simulScore = score

    if direc != direcList[1]:
        if direc ==5:
            orin = direcList[1]
        newMap = copy.deepcopy(list_map)
        move2(newMap, direcList[1], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation2(newMap, depth + 1, simulScore, direcList[1], orin)


        simulScore = score

    if direc != direcList[2]:
        if direc ==5:
            orin = direcList[2]
        newMap = copy.deepcopy(list_map)
        move2(newMap, direcList[2], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation2(newMap, depth + 1, simulScore, direcList[2], orin)
        simulScore = score

    if direc != direcList[3]:
        if direc ==5:
            orin = direcList[3]
        newMap = copy.deepcopy(list_map)
        move2(newMap, direcList[3], simulScore)
        if maxSimul < simulScore:
            maxSimul = simulScore
            minDepth = depth
            code = orin
        elif maxSimul == simulScore:
            if minDepth > depth:
                maxSimul = simulScore
                minDepth = depth
                code = orin
        simulation2(newMap, depth + 1, simulScore, direcList[3], orin)
        simulScore = score


    return code

def countTwoFour(list_map):
    count = 0
    for i in range(4):
        for j in range(4):
            if list_map[i][j] == 2 or list_map[i][j] == 4:
                count = count +1
    return count


def runGame():
    global done, gameOver, maxSimul, minDepth, code

    list_map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    null_list = []

    for i in range(4):
        for j in range(4):
            null_list.append([i, j])

    random.shuffle(null_list)

    coord = null_list[0]
    del null_list[0]
    list_map[coord[0]][coord[1]] = 2

    coord = null_list[0]
    del null_list[0]
    list_map[coord[0]][coord[1]] = 2

    list_map_coord = [[[100, 100], [300, 100], [500, 100], [700, 100]],
                      [[100, 300], [300, 300], [500, 300], [700, 300]],
                      [[100, 500], [300, 500], [500, 500], [700, 500]],
                      [[100, 700], [300, 700], [500, 700], [700, 700]]]

    myFont = pygame.font.SysFont("arial", 100)
    gameOverFont = pygame.font.SysFont("arial", 150)

    while not done:
        text_Titles = []

        screen.fill(WHITE)

        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 0, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(400, 0, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(600, 0, 200, 200), 1)
        #
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 200, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 200, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(400, 200, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(600, 200, 200, 200), 1)
        #
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 400, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 400, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(400, 400, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(600, 400, 200, 200), 1)

        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 600, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 600, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(400, 600, 200, 200), 1)
        pygame.draw.rect(screen, BLACK, pygame.Rect(600, 600, 200, 200), 1)

        for i in range(4):
            for j in range(4):
                if list_map[i][j] != 0:
                    text_Title = myFont.render(str(list_map[i][j]), True, BLACK)
                    text_Rect = text_Title.get_rect()
                    text_Rect.centerx = list_map_coord[i][j][0]
                    text_Rect.centery = list_map_coord[i][j][1]
                    screen.blit(text_Title, text_Rect)

        text = myFont.render("score = ["+str(mainscore)+"]", True, BLACK)
        text_Rect = text.get_rect()
        text_Rect.centerx = 400
        text_Rect.centery = 900
        screen.blit(text, text_Rect)

        if gameOver:
            text = gameOverFont.render(" Game Over ", True, RED)
            text_Rect = text.get_rect()
            text_Rect.centerx = 400
            text_Rect.centery = 400
            screen.blit(text, text_Rect)


        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:


                if event.key != pygame.K_UP and event.key != pygame.K_DOWN and event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT and event.key != pygame.K_SPACE:
                    break

                if event.key == pygame.K_UP:
                    if not move(list_map, 2, mainscore, True):
                        break

                elif event.key == pygame.K_DOWN:
                    if not move(list_map, 3, mainscore, True):
                        break

                elif event.key == pygame.K_LEFT:
                    if not move(list_map, 0, mainscore, True):
                        break

                elif event.key == pygame.K_RIGHT:
                    if not move(list_map, 1,mainscore, True):
                        break

                elif event.key == pygame.K_SPACE:
                    code = random.randrange(0,4)
                    maxSimul = 0
                    minDepth = 100
                    minTwoandFour =20
                    #simulScore = 0
                    simulScore = mainscore

                    simulation(list_map, 0, mainscore,  5, 5)

                    #(list_map, 0, 0, 5, 5)
                    if not move(list_map, code, mainscore, True):
                        code = random.randrange(0,4)
                        if not move(list_map, code, mainscore, True):
                            break

                null_list = []
                for i in range(4):
                    for j in range(4):
                        if list_map[i][j] == 0:
                            null_list.append([i, j])
                if len(null_list) > 0:
                    random.shuffle(null_list)
                    coord = null_list[0]
                    del null_list[0]
                    list_map[coord[0]][coord[1]] = random.choice([2, 4])

                newMap = copy.deepcopy(list_map)

                #이건 게임 오버
                if not move(newMap, 1, mainscore) and not move(newMap, 0, mainscore) and not move(newMap, 2, mainscore) and not move(newMap, 3, mainscore):

                    print("your score is "+str(mainscore))
                    gameOver = True




runGame()
pygame.quit()
