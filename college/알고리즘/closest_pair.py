import math
def get_dist(point_a,point_b):
    return math.dist(point_a,point_b)

def closest_pair(S):
    i = len(S)
    if(i<=3):
        answer = []
        for j in range(i-1):
            answer.append(get_dist(S[j],S[j+1]))
        return min(answer)
    mid = i // 2
    S_L = S[:mid]
    S_R = S[mid:]
    CP_L = closest_pair(S_L)
    CP_R = closest_pair(S_R)
    d = int(min(CP_R,CP_L))
    
    S_M = S[i//2-d:i//2+d]
    CP_M = closest_pair(S_M)
    return (min(CP_L,CP_M,CP_R))
print(closest_pair([[1,1],[1,3],[5,1],[7,1]]))
    
         