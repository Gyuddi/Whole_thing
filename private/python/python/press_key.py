def solution(numbers, hand):
    left_hand = 10
    right_hand = 12
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            left_hand = n
        elif n in [3,6,9]:
            answer += "R"
            right_hand = n
        else:
            if n == 0:
                n = 11
            absL = abs(n-left_hand)
            absR = abs(n-right_hand)
            if sum(divmod(absL,3)) > sum(divmod(absR,3)):
                answer += "R"
                right_hand = n
            elif sum(divmod(absL,3)) < sum(divmod(absR,3)):
                answer += "L"
                left_hand = n
            else:
                if hand == "left":
                    answer += "L"
                    left_hand = n
                elif hand =="right":
                    answer += "R"
                    right_hand = n
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))
