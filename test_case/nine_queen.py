def check_position(prior_list: list, next_coordinate: list):
    for i in prior_list:
        if abs(i[1] - next_coordinate[1]) in (0, abs(i[0] - next_coordinate[0])): #不需要考虑同一行的情况
            return False
    return True


result: list = []
chessboard_scale: int = 8
chess_num:int = 8


def Eight_Queen(num: int, each_result: list):
    print(each_result)
    for i in range(chessboard_scale):
        current_pos:list = [num , i]
        if check_position(prior_list=each_result, next_coordinate=current_pos):
            if num == chess_num - 1:
                each_result.append(current_pos)
                result.append(each_result)
                return
            else:
                Eight_Queen(num + 1, each_result + [current_pos])
    return

Eight_Queen(0, [])
print(len(result))
def show_chackerboard(result:list):
    chessboard:list = [['*' for _ in range(chessboard_scale)] for __ in range(chessboard_scale)]
    for i in result:
        for j in i:
            chessboard[j[0]][j[1]] = "@"
        [print(i[j],end='\t') if j!=len(i) else print() for i in chessboard for j in range(len(i)+1)]
        chessboard = [['*' for _ in range(chessboard_scale)] for __ in range(chessboard_scale)]
        print(f"<{'-'*30}>")

show_chackerboard(result)