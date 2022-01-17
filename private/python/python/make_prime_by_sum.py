def solution(nums):
    answer = []
    summ = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                summ.append(nums[i]+nums[j]+nums[k])
    print(summ) 

    for i in summ:
        count = 0
        for j in range(2,i):
            if i % j ==0:
                count += 1
        if count == 0 :
            answer.append(i)
    return len(answer)
nums = [1,2,7,6,4]
print(solution(nums))