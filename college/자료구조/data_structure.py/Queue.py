class Queue:
    def __init__(self):
        self.q = []
    def getSize(self):
        return len(self.q)
    def isEmpty(self):
        return len(self.q) == 0
    def enQueue(self, item):
        self.q.append(item)
    def deQueue(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)
    def peek(self):
        return self.q[0]
    def peek_last(self):
        return self.q[-1]

#지수분포? 단위 시간당 평균 발생 횟수가 lamda일때, 사건이 처음 발생할
# 때까지 걸리는 시간이 T 이하일 확률 
# import numpy as np
# x = np.random.exponential(1, 10)
# entTime = np.cumsum(x)
# cafe = Queue()
# delay_time = 0
def come_and_out(entTime,cafe):
    print(entTime)
    for i in range(len(entTime)):
        if cafe.isEmpty() == True:
            cafe.enQueue(entTime[i]+1)
            print(cafe.q)
            print(cafe.getSize())
        else:
            if entTime[i] >= cafe.peek_last():
                cafe.enQueue(entTime[i]+1)
                while entTime[i] > cafe.peek():
                    cafe.deQueue()
                print(cafe.q,cafe.getSize())
                
            else:
                while entTime[i] > cafe.peek():
                    cafe.deQueue()
                delay_time = cafe.peek_last()+1
                cafe.enQueue(delay_time)
                print(cafe.q,cafe.getSize())

        if cafe.peek_last() > 14*6:
            break
# come_and_out(entTime)


# 2시에서 4시까지 손님의 빈도가 2배로 증가한다면?

# import numpy as np
# x = np.random.exponential(1, 10)
# entTime = np.cumsum(x)
# y = np.random.exponential(0.5, 20)
# lunch_entTime = np.cumsum(y)
# whole_time = []
# for time in entTime:
#     if time >= 6:
#         break
#     whole_time.append(time)

# for l_time in lunch_entTime:
#     if l_time >=6:
#         if l_time > 8 :
#             break
#         whole_time.append(l_time)

# for time in entTime:
#     if time >= 8:
#         whole_time.append(time)
# cafe = Queue()
# delay_time = 0
# come_and_out(whole_time)

#점원이 두명일때
import numpy as np
x = np.random.exponential(1, 10)
entTime = np.cumsum(x)
cafe1 = Queue()
cafe2 = Queue()
delay_time = 0
print(entTime)
for i in range(len(entTime)):
    if cafe1.isEmpty() == True:
        cafe1.enQueue(entTime[i]+1)
        print("점원1=",cafe1.q,cafe1.getSize())
        print("점원2=",cafe2.q,cafe2.getSize())
    elif cafe2.isEmpty() == True:
        cafe2.enQueue(entTime[i]+1)
        print("점원1=",cafe1.q,cafe1.getSize())
        print("점원2=",cafe2.q,cafe2.getSize())
    elif cafe1.peek_last() < cafe2.peek_last():
        if entTime[i] >= cafe1.peek_last():
            cafe1.enQueue(entTime[i]+1)
            while entTime[i] > cafe1.peek():
                cafe1.deQueue()
            print("점원1=",cafe1.q,cafe1.getSize())                
        else:
            while entTime[i] > cafe1.peek():
                cafe1.deQueue()
            delay_time = cafe1.peek_last()+1
            cafe1.enQueue(delay_time)
            print("점원1=",cafe1.q,cafe1.getSize())
    elif cafe1.peek_last() > cafe2.peek_last():
        if entTime[i] >= cafe2.peek_last():
            cafe2.enQueue(entTime[i]+1)
            while entTime[i] > cafe2.peek():
                cafe2.deQueue()
            print("점원2=",cafe2.q,cafe2.getSize())                
        else:
            while entTime[i] > cafe2.peek():
                cafe2.deQueue()
            delay_time = cafe2.peek_last()+1
            cafe2.enQueue(delay_time)
            print("점원2=",cafe2.q,cafe2.getSize())

    if cafe1.peek_last() > 14*6 and cafe2.peek_last() > 14*6:
        break