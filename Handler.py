import config


def getCellsAbsolutePosition(piece):
    '''取得方塊當前所有方格的座標'''
    return [(y + piece.y, x + piece.x) for y, x in piece.getCells()]


def fixPiece(shot, piece):
    '''固定已落地的方塊，並且在main中自動切到下一個方塊'''
    piece.is_fixed = True
    for y, x in getCellsAbsolutePosition(piece):
        shot.status[y][x] = 2
        shot.color[y][x] = piece.color


### Your homework below. Enjoy :) ###

def moveLeft(shot, piece):
    # here，在這裡填入 code
    move=True
    for y, x in getCellsAbsolutePosition(piece):
        if x == 0 or shot.status[y][x - 1] == 2:
            move=False
    if move:    
        piece.x -= 1
    pass


def moveRight(shot, piece):
    # here
    move=True
    for y, x in getCellsAbsolutePosition(piece):
        if x +1== config.columns or shot.status[y][x + 1] == 2:
            move=False
    if move:
        piece.x += 1
    pass


def drop(shot, piece):
    # here

    for y, x in getCellsAbsolutePosition(piece):
        if y>=0:
            if y == 19 or shot.status[y + 1][x] == 2:
                fixPiece(shot, piece)
    piece.y += 1
    pass

# 瞬間掉落


def instantDrop(shot, piece):
    for i in range(20):
        for y, x in getCellsAbsolutePosition(piece):
            if y+1 == config.rows or shot.status[y+1][x] == 2:
                fixPiece(shot, piece)
                return
        piece.y += 1
    pass

# 旋轉方塊


def rotate(shot, piece):

    piece.rotation += 1
    for y, x in getCellsAbsolutePosition(piece):

        if x >= 10 or x < 0 or shot.status[y][x] == 2:
            piece.rotation -= 1
            return
    pass

# 判斷是否死掉（出局）


def isDefeat(shot, piece):
    for y, x in getCellsAbsolutePosition(piece):
        if shot.status[y][x] == 2 and y >= 0 and y==0:
            return True
        else:
            return False
    pass

# 消去列


def eliminateFilledRows(shot, piece):
    line = 0
    line1 = 0
    score=0
    el=False
    for y in range(config.rows):
        a = 0
        for x in range(config.columns):
            if shot.status[y][x] == 2:
                a += 1
        if a == 10:
            el=True
            
            
            if el==True:
                line1= shot.line_count
                shot.line_count += 1
                line +=1
            else:
                line=0

            for k in range(10):
                for i in range(y, 0, -1):
                    shot.status[i][k] = shot.status[i-1][k]

    shot.score += config.score_count.get(line,0)
    pass
