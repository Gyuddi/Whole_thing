import random
def broiling(broiler_number, weight, patty_weights):
    answer = 0
    patty_weights_one = random.randrange(20,30)
    patty = 0
    patty_weights = patty * patty_weights_one  # patty_weights_one은 패티 하나의 무게 patty는 주문에 따라 구워야하는 패티의 갯수
    broiler = [0] * broiler_number
    time = 0
    while len(broiler) != 0:
        broiler_number >= 20
        time += 2
        broiler.pop(0)
        if patty_weights:
            if sum(broiler) + patty_weights[0] <= weight:
                broiler.append(patty_weights[0])
                patty_weights.pop(0)
            else:
                broiler.append(0)
    return time

print(broiling(20, 30, 2))
print()


for i in r