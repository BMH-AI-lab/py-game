from .character import Character

class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level, health=100, attack_power=15)

    def attack(self, target):
        dmg = self.attack_power
        print(f"{self.name} 기본 공격! ({dmg})")
        target.take_damage(dmg)

    def special_attack(self, target):
        dmg = self.attack_power * 2
        print(f"{self.name} 특수공격 [강력한 일격]! ({dmg})")
        target.take_damage(dmg)
        self.health = max(0, self.health - 5)
        print(f"{self.name} 반동으로 체력 -5 (현재 {self.health})")
