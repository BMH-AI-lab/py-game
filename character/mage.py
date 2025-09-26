from .character import Character
from exceptions.errors import ManaError   # ← 패키지 루트 기준 절대 import

class Mage(Character):
    # 클래스 상속
    # 마법사의 기본 캐릭터 구성(이름, 레벨, 체력, 공격력) , 마나를 100으로 설정 
    def __init__(self, name, level=1):
        super().__init__(name, level, health=80, attack_power=18)
        self.mana = 100

    # 기본 공격: 마법사의 공격력 만큼 상대의 체력을 뻇음 
    def attack(self, target):
        dmg = self.attack_power
        print(f"{self.name} 마법탄! ({dmg})")
        target.take_damage(dmg)

    # 특수 공격: 20의 마나로 파이어볼 발사, 20의 마나를 줄임  
    # 마나가 20미만 이면 마나 부족 메세지  
    def special_attack(self, target):
        if self.mana < 20:
            raise ManaError(f"{self.name}의 마나가 부족합니다! (현재 {self.mana})")
        # 특수 공격 시 1.5배 공격력
        dmg = int(self.attack_power * 1.5)
        # 20 마나 소비 
        self.mana -= 20
        # 특수 공격을 하면 남은 마나 수치 출력 
        print(f"{self.name} 특수공격 [파이어볼]! ({dmg}), 남은 마나:{self.mana}")
        target.take_damage(dmg)
        
    # 남은 체력과 공격력, 마나량 출력 
    def show_status(self):
        print(f"[{self.name}] 체력:{self.health}/{self.max_health}, 공격력:{self.attack_power}, 마나:{self.mana}")
