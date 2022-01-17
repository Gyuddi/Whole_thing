def solution(n, lost, reserve):

    answer = 0
    answer = n - len(lost)

    for i in lost:
        if i in reserve:
            answer = answer+1
            reserve.remove(i)
            continue
        for j in reserve:
            if j == i-1:
                answer +=1
                reserve.remove(j)
                break
            if j ==i+1:
                if j in lost:
                    break
                answer+=1
                reserve.remove(j)
                break
        

    return answer

n=8
lost=[1,2,4,6]
reserve=[1,2,4,6]
print(solution(n, lost, reserve))