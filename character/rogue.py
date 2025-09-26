import random
from .character import Character

class Rogue(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level, health=90, attack_power=12)

    def attack(self, target):
        dmg = self.attack_power
        print(f"{self.name} 기본 공격! ({dmg})")
        target.take_damage(dmg)

    def special_attack(self, target):
        if random.random() <= 0.7:
            dmg = self.attack_power * 3
            print(f"{self.name} 특수공격 [급습] 성공! ({dmg})")
            target.take_damage(dmg)
        else:
            print(f"{self.name} [급습] 빗나감!")
