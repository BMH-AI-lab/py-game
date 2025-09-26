import random
from .character import Character

class Rogue(Character):
    # 부모 클래스 상속
    # 도적의 기본 능력치(이름, 레벨 ,체력, 공격력)
    def __init__(self, name, level=1):
        super().__init__(name, level, health=90, attack_power=12)

    # 기본 공격
    # 기본 공격을 하면 공격령 만큼 상대 체력을 줄임
    def attack(self, target):
        dmg = self.attack_power
        print(f"{self.name} 기본 공격! ({dmg})")
        target.take_damage(dmg)
  
    # 특수 공격
    def special_attack(self, target):
    # 급습을 70% 이하의 확률로 성공할지 실패할지 랜덤으로 설정
    # 성공하면 성공메세지가 뜨고 실패하면 실패 메세지가 출력
        if random.random() <= 0.7:
            dmg = self.attack_power * 3
            print(f"{self.name} 특수공격 [급습] 성공! ({dmg})")
            target.take_damage(dmg)
        else:
            print(f"{self.name} [급습] 빗나감!")
