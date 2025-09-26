from .character import Character
from exceptions.errors import ManaError   # ← 패키지 루트 기준 절대 import

class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level, health=80, attack_power=18)
        self.mana = 100

    def attack(self, target):
        dmg = self.attack_power
        print(f"{self.name} 마법탄! ({dmg})")
        target.take_damage(dmg)

    def special_attack(self, target):
        if self.mana < 20:
            raise ManaError(f"{self.name}의 마나가 부족합니다! (현재 {self.mana})")
        dmg = int(self.attack_power * 1.5)
        self.mana -= 20
        print(f"{self.name} 특수공격 [파이어볼]! ({dmg}), 남은 마나:{self.mana}")
        target.take_damage(dmg)

    def show_status(self):
        print(f"[{self.name}] 체력:{self.health}/{self.max_health}, 공격력:{self.attack_power}, 마나:{self.mana}")
