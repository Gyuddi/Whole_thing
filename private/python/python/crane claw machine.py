# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

def solution(board, moves):
    answer = 0
    result = []
    character =""
    
    for move in moves:
        for j in range(len(board)):
            character = board[j][move-1]
            if character == 0:
                pass
            else :
                result.append(character)
                board[j][move-1] = 0
                break
        # while True:
        #     if len(result) > 1 and result[-1] == result[-2]:
        #         result.pop()
        #         result.pop()
        #         answer += 2
        #     else :
        #         break

    while True:
        for i in range(len(result)-1):
            if result[i] == result[i+1]:
                answer += 2
                del result[i]
                del result[i+1]
                break
        else:
            break
    return answer,result



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))