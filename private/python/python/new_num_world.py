def solution(n):
    answer = ""
    num_list = ["1","2","4"]
    if n <= 3:
        answer = num_list[(n%3)-1]
    else:
        m,n = divmod(n,3)
        if n == 0:
            answer = num_list[m%3-2] + num_list[n-1]
        else:
            answer = solution(m-1) + num_list[n-1]
    return answer

print(solution(1))