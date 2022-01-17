def solution(priorities, location):
    answer = 0
    num_set = []
    new_set = []
    for idx,value in enumerate(priorities):
        num_set.append((value,idx))
    target = num_set[location]

    while len(num_set) != 0:
        if num_set[0][0] == max(priorities):
            new_set.append(num_set.pop(0))
            priorities.remove(max(priorities))
        else:
            num_set.append(num_set.pop(0))
    return new_set.index(target) +1
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))