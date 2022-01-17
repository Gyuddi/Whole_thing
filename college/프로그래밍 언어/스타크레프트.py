import random
class Unit:
    def __init__(self,name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{}유닛이 생성되었습니다.".format(self.name))

    def move(self,location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{} : {}데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{} : 현재 채력은 {}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다".format(self.name))

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력{}]"\
              .format(self.name,location,self.damage))

class marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp >= 10:
            self.hp -= 10
            print("{} : 스팀팩 사용".format(self.name))
        else:
            print("{} : 스팀팩 사용이 불가능합니다".format(self.name))

class tank(AttackUnit):

    seize = False
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

    def set_seize(self):
        if tank.seize == False:
            return
        if self.seize_mode == False:
            print("{} : 시즈모드 전환합니다".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{} : 시즈모드 헤제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False



class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
              .format(name,location,self.flying_speed))

class FlyableAttack(AttackUnit, Flyable):
        def __init__(self,name,hp,damage,flying_speed):
            AttackUnit.__init__(self,name,hp,0,damage)
            Flyable.__init__(self,flying_speed)

        def move(self,location):
            print("[공중유닛 이동]")
            self.fly(self.name,location)

class wraith(FlyableAttack):
    def __init__(self):
        FlyableAttack.__init__(self,"레이스",80,20,5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹모드 실행합니다".format(self.name))
            self.clocked = False

        else:
            print("{} : 클로킹모드 헤제합니다".format(self.name))
            self.clocked = True

def game_start():
    print("새로운 게임을 시작합니다")

def game_over():
    print("GG")
    print("상대방이 게임에서 퇴장했습니다")


#실제 게임 진행

game_start()

m1=marine()
m2=marine()
m3=marine()

t1=tank()
t2=tank()

w1=wraith()
w2=wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군이동
for unit in attack_units:
    unit.move("1시")

tank.seize = True
print("탱크 시즈모드 개발 완료")

for unit in attack_units:
    if isinstance(unit,marine):
        unit.stimpack()
    elif isinstance(unit,tank):
        unit.set_seize()
    elif isinstance(unit,wraith):
        unit.clocking()


for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(random.randint(5,21))

game_over()

