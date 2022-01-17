class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed

    def move (self,location):
        print("지상유닛 이동")
        print("{}:{}방향으로 이동합니다.[속도{}]"\
            .format(self.name,location,self.speed))

class attackunit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

    def attack(self,location):
        print("{}:{} 방향으로 적군을 공격합니다.공격력:{}"\
            .format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{}:{}데미지를 입었습니다."\
            .format(self.name,damage))
        self.hp=self.hp-damage
        print("{}:현재의 체력은 {}입니다".format(self.name,self.hp))
        if self.hp<=0:
            print("{}:파괴되었습니다.".format(self.name))


class flyable:
    def __init__(self,f_speed):
        self.f_speed=f_speed

    def fly(self,name,location):
        print("{}:{}방향으로 날아갑니다.[속도{}]"\
            .format(name,location,self.f_speed))

class flyableattack(attackunit,flyable):
    def __init__(self,name,hp,damage,f_speed):
        attackunit.__init__(self,name,hp,0,damage)
        flyable.__init__(self,f_speed)

    def move(self,location):
        print("공중유닛이동")
        self.fly(self.name,location)


vulture=attackunit("벌쳐",80,2,20)

battlecr=flyableattack("배틀크루저",500,25,3)

vulture.move("11시")
battlecr.move("9시")
        
