import pygame  # 1. pygame 선언
import random
import copy

pygame.init()  # 2. pygame 초기화

size = [800, 1000]
done = False
gameOver = False

mainscore = 0
simulScore = 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048 with AI")


# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
ORANGE = (int("ff",16), int("7f",16),0)

clock = pygame.time.Clock()


def move(map, direc, score, mode= False):
    success = False
    global mainscore, simulScore

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


def simulation(list_map, depth, score, direc, maxDepth=7):
    global simulScore, code

    if depth == maxDepth:
        return (direc, countZero(list_map), score)

    simulScore = score
    scoreSum = []
    zeroSum = []
    AllSum = []
    tempScore =0
    tempZero =0

    if depth==0:
        zeroCount = countZero(list_map)

        if zeroCount>12:
            maxDepth = 2
        if zeroCount>9:
            maxDepth = 3
        elif zeroCount>6:
            maxDepth = 5

    else:
        null_list = []
        for i in range(4):
            for j in range(4):
                if list_map[i][j] == 0:
                    null_list.append([i, j])
        if len(null_list) > 0:
            random.shuffle(null_list)
            coord = null_list[0]
            del null_list[0]
            list_map[coord[0]][coord[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])


    if direc != 0:
        newMap = copy.deepcopy(list_map)
        move(newMap, 0, simulScore)

        (code, tempZero, tempScore) = simulation(newMap, depth + 1, simulScore, 0,maxDepth)
        zeroSum.append(tempZero)
        scoreSum.append(tempScore)
        simulScore = score


    if direc != 1:
        newMap = copy.deepcopy(list_map)
        move(newMap, 1, simulScore)

        (code, tempZero, tempScore) = simulation(newMap, depth + 1, simulScore, 1,maxDepth)
        zeroSum.append(tempZero)
        scoreSum.append(tempScore)

        simulScore = score

    if direc != 2:
        newMap = copy.deepcopy(list_map)
        move(newMap, 2, simulScore)

        (code, tempZero, tempScore) = simulation(newMap, depth + 1, simulScore,2,maxDepth)
        zeroSum.append(tempZero)
        scoreSum.append(tempScore)

        simulScore = score

    if direc != 3:
        newMap = copy.deepcopy(list_map)
        move(newMap, 3, simulScore)

        (code, tempZero, tempScore) = simulation(newMap, depth + 1, simulScore, 3,maxDepth)
        zeroSum.append(tempZero)
        scoreSum.append(tempScore)

        simulScore = score

    for i in range(len(zeroSum)):
        AllSum.append(zeroSum[i]*2+scoreSum[i])

    if depth ==0:
        code = AllSum.index(max(AllSum))

    # if depth ==0:
    #     if scoreSum.index(max(scoreSum)) != AllSum.index(max(AllSum)):
    #         for i in range(4):
    #             print(str(scoreSum[i])+" , "+str(zeroSum[i]*3))
    #         print("\n\n_________\n\n")

    return code, sum(zeroSum), sum(scoreSum)


def countZero(map):
    count =0
    for i in range(4):
        for j in range(4):
            if map[i][j] ==0:
                count = count+1
    return count


def runGame(test=False):

    global done, gameOver, code

    list_map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    null_list = []

    for i in range(4):
        for j in range(4):
            null_list.append([i, j])

    random.shuffle(null_list)

    coord = null_list[0]
    del null_list[0]
    list_map[coord[0]][coord[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

    coord = null_list[0]
    del null_list[0]
    list_map[coord[0]][coord[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

    list_map_coord = [[[100, 100], [300, 100], [500, 100], [700, 100]],
                      [[100, 300], [300, 300], [500, 300], [700, 300]],
                      [[100, 500], [300, 500], [500, 500], [700, 500]],
                      [[100, 700], [300, 700], [500, 700], [700, 700]]]

    myFont = pygame.font.SysFont("arial", 100)
    gameOverFont = pygame.font.SysFont("arial", 150)

    while not done:

        screen.fill(WHITE)


        for i in range(4):
            for j in range(4):
                pygame.draw.rect(screen, BLACK, pygame.Rect(j*200, i*200, 200, 200), 1)


        for i in range(4):
            for j in range(4):
                if list_map[i][j] != 0:
                    text_Title = myFont.render(str(list_map[i][j]), True, ORANGE)
                    text_Rect = text_Title.get_rect()
                    text_Rect.centerx = list_map_coord[i][j][0]
                    text_Rect.centery = list_map_coord[i][j][1]
                    screen.blit(text_Title, text_Rect)

        text = myFont.render("score = [" + str(mainscore) + "]", True, BLACK)
        text_Rect = text.get_rect()
        text_Rect.centerx = 400
        text_Rect.centery = 900
        screen.blit(text, text_Rect)

        if gameOver:
            if test:
                return mainscore
            text = gameOverFont.render(" Game Over ", True, RED)
            text_Rect = text.get_rect()
            text_Rect.centerx = 400
            text_Rect.centery = 400
            screen.blit(text, text_Rect)

        pygame.display.update()
        clock.tick(30)


        if test:
            code = random.randrange(0, 4)
            simulScore = mainscore
            (code, zerotemp, scoretemp)  = simulation(list_map, 0, mainscore, 5)

            if not move(list_map, code, mainscore, True):
                code = random.randrange(0, 4)
                move(list_map, code, mainscore, True)
            null_list = []
            for i in range(4):
                for j in range(4):
                    if list_map[i][j] == 0:
                        null_list.append([i, j])
            if len(null_list) > 0:
                random.shuffle(null_list)
                coord = null_list[0]
                del null_list[0]
                list_map[coord[0]][coord[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

            newMap = copy.deepcopy(list_map)

            # 이건 게임 오버
            if not move(newMap, 1, mainscore) and not move(newMap, 0, mainscore) and not move(newMap, 2,                                                                    mainscore) and not move(
                newMap, 3, mainscore):
                print("your score is " + str(mainscore))
                gameOver = True


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
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
                        if not move(list_map, 1, mainscore, True):
                            break

                    elif event.key == pygame.K_SPACE:

                        (code, zerotemp, scoretemp) = simulation(list_map, 0, mainscore, 5)
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
                        list_map[coord[0]][coord[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

                    newMap = copy.deepcopy(list_map)

                    # 이건 게임 오버
                    if not move(newMap, 1, mainscore) and not move(newMap, 0, mainscore) and not move(newMap, 2, mainscore) and not move(newMap, 3, mainscore):
                        print("your score is " + str(mainscore))
                        gameOver = True





isTest = input("1.일반모드 2.테스트 모드>>")

if isTest == "2":

    testData = []
    for i in range(5):
        mainscore = 0
        gameOver = False
        testData.append(runGame(True))

    print("최고점 = " + repr(max(testData)))
    print("평균 : " + repr((sum(testData) / len(testData))))

else:
    runGame()


# testData = []
# for i in range(5):
#     mainscore = 0
#     gameOver = False
#     testData.append(runGame(True))
#
# print("최고점 = " + repr(max(testData)))
# print("평균 : " + repr((sum(testData) / len(testData))))
#
# pygame.quit()



#시뮬 버전 2

# def simulation(list_map, depth, score, direc, orin,maxDepth=7):
#     global simulScore, maxSimul, minDepth
#     global code
#
#     simulScore = score
#     scoreSum = []
#     tempScore =0
#     direcList =[0,1,2,3]
#     random.shuffle(direcList)
#
#     if depth==0:
#         zeroCount = 0
#         for i in range(4):
#             for j in range(4):
#                 if list_map[i][j] ==0:
#                     zeroCount = zeroCount +1
#
#         if zeroCount>9:
#             maxDepth = 3
#         elif zeroCount>6:
#             maxDepth = 5
#
#     else:
#         null_list = []
#         for i in range(4):
#             for j in range(4):
#                 if list_map[i][j] == 0:
#                     null_list.append([i, j])
#         if len(null_list) > 0:
#             random.shuffle(null_list)
#             coord = null_list[0]
#             del null_list[0]
#             list_map[coord[0]][coord[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
#
#
#     if depth == maxDepth:
#         return (orin, score)
#
#     if direc != direcList[0]:
#         if direc ==5:
#             orin = direcList[0]
#         newMap = copy.deepcopy(list_map)
#
#         move(newMap, direcList[0], simulScore)
#
#         (code, tempScore) = simulation(newMap, depth + 1, simulScore, direcList[0], orin,maxDepth)
#         scoreSum.append(tempScore)
#         simulScore = score
#
#     if direc != direcList[1]:
#         if direc ==5:
#             orin = direcList[1]
#         newMap = copy.deepcopy(list_map)
#         move(newMap, direcList[1], simulScore)
#         (code, tempScore) = simulation(newMap, depth + 1, simulScore, direcList[1], orin,maxDepth)
#         scoreSum.append(tempScore)
#
#         simulScore = score
#
#     if direc != direcList[2]:
#         if direc ==5:
#             orin = direcList[2]
#         newMap = copy.deepcopy(list_map)
#         move(newMap, direcList[2], simulScore)
#         (code, tempScore) = simulation(newMap, depth + 1, simulScore, direcList[2], orin,maxDepth)
#         scoreSum.append(tempScore)
#         simulScore = score
#
#     if direc != direcList[3]:
#         if direc ==5:
#             orin = direcList[3]
#         newMap = copy.deepcopy(list_map)
#         move(newMap, direcList[3], simulScore)
#         (code, tempScore) = simulation(newMap, depth + 1, simulScore, direcList[3], orin,maxDepth)
#         scoreSum.append(tempScore)
#         simulScore = score
#
#
#     if depth ==0:
#         code = direcList[scoreSum.index(max(scoreSum))]
#     return (code, sum(scoreSum))



#기존 시뮬레이션 함수 테스트

# #처음엔 시뮬레이션으로 최댓값이 오게 설정을 하게되었는데 depth에 따라 과 시뮬레이션으로 모두 동점을 받을 수있음
# #그렇다고 depth 임계치를 낮추면 정확도가 적거나, 최적해를 반영하기 힘듬.
# # 따라서 시뮬레이션에서 최댓값 + 그 최댓값의 최소 깊이를 반영해야 함.
# # 첫 번째 시뮬레이션은 지금 당장 높은 점수를 얻는 방향으로 진행됨.  두번째 시뮬레이션은 빈칸을 늘리는 방향으로 진행할 예정
#
# def simulation(list_map, depth, score, direc, orin):
#     global simulScore, maxSimul, minDepth
#     global code
#
#     simulScore = score
#     direcList =[0,1,2,3]
#     random.shuffle(direcList)
#
#     if depth == 8:
#         return
#
#     if direc != direcList[0]:
#         if direc ==5:
#             orin = direcList[0]
#         newMap = copy.deepcopy(list_map)
#
#         move(newMap, direcList[0], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation(newMap, depth + 1, simulScore, direcList[0], orin)
#
#         simulScore = score
#
#     if direc != direcList[1]:
#         if direc ==5:
#             orin = direcList[1]
#         newMap = copy.deepcopy(list_map)
#         move(newMap, direcList[1], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation(newMap, depth + 1, simulScore, direcList[1], orin)
#
#
#         simulScore = score
#
#     if direc != direcList[2]:
#         if direc ==5:
#             orin = direcList[2]
#         newMap = copy.deepcopy(list_map)
#         move(newMap, direcList[2], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation(newMap, depth + 1, simulScore, direcList[2], orin)
#         simulScore = score
#
#     if direc != direcList[3]:
#         if direc ==5:
#             orin = direcList[3]
#         newMap = copy.deepcopy(list_map)
#         move(newMap, direcList[3], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation(newMap, depth + 1, simulScore, direcList[3], orin)
#         simulScore = score
#
#     return code
#
#
#
# #공평하게 갯수를 가장 많이 줄이는것에 초점을 둬본다.
# def simulation2(list_map, depth, score, direc, orin):
#     global simulScore, maxSimul, minDepth
#     global code
#
#     simulScore = score
#     direcList =[0,1,2,3]
#     random.shuffle(direcList)       #비교순서의 편향을 방지
#
#     if depth == 8:
#         return
#
#     if direc != direcList[0]:
#         if direc ==5:
#             orin = direcList[0]
#         newMap = copy.deepcopy(list_map)
#
#         move2(newMap, direcList[0], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation2(newMap, depth + 1, simulScore, direcList[0], orin)
#
#         simulScore = score
#
#     if direc != direcList[1]:
#         if direc ==5:
#             orin = direcList[1]
#         newMap = copy.deepcopy(list_map)
#         move2(newMap, direcList[1], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation2(newMap, depth + 1, simulScore, direcList[1], orin)
#
#
#         simulScore = score
#
#     if direc != direcList[2]:
#         if direc ==5:
#             orin = direcList[2]
#         newMap = copy.deepcopy(list_map)
#         move2(newMap, direcList[2], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation2(newMap, depth + 1, simulScore, direcList[2], orin)
#         simulScore = score
#
#     if direc != direcList[3]:
#         if direc ==5:
#             orin = direcList[3]
#         newMap = copy.deepcopy(list_map)
#         move2(newMap, direcList[3], simulScore)
#         if maxSimul < simulScore:
#             maxSimul = simulScore
#             minDepth = depth
#             code = orin
#         elif maxSimul == simulScore:
#             if minDepth > depth:
#                 maxSimul = simulScore
#                 minDepth = depth
#                 code = orin
#         simulation2(newMap, depth + 1, simulScore, direcList[3], orin)
#         simulScore = score
#
#
#     return code
#
# def countTwoFour(list_map):
#     count = 0
#     for i in range(4):
#         for j in range(4):
#             if list_map[i][j] == 2 or list_map[i][j] == 4:
#                 count = count +1
#     return count