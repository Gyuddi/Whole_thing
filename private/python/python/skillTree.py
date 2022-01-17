def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for i in skill_trees:
        new_skill = []
        for s in skill:
            new_skill.append(s)
        work = True
        for j in i:
            if new_skill:
                if j == new_skill[0]:
                    new_skill.pop(0)
                    
                elif j in new_skill and j != new_skill[0]:
                    work = False
        if work == True:
            answer += 1
    return answer
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))