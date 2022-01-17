def solution(nums):
    answer = []
    select = len(nums)/2
    count = 0
    for i in nums:
        if i not in answer:
            answer.append(i)
            count += 1
            if count == select:
                break
    return len(answer)

nums = [3,3,3,2,2,4]
print(solution(nums))