def solution(a, b):
    days = 0
    monthdays = [31,29,31,30,31,30,31,31,30,31,30,31]
    day_list = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    for i in range(a-1):
        days += monthdays[i]
    days += b
    answer = day_list[days%7-1]

    return answer
a=5
b=24
print(solution(a, b))