def solution(n):
    if (n**0.5) != int(n ** 0.5):
        answer = -1
    else:
        answer = ((n**0.5)+1)**2
    return answer