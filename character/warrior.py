from .character import Character

class Warrior(Character):
    # 캐릭터 상속 및 전사의 기본 능력치 
    def __init__(self, name, level=1):
        super().__init__(name, level, health=100, attack_power=15)

    # 기본 공격: 공격력만큼 피해를 주면서 상대 캐릭터의 체력을 감소시킴
    def attack(self, target):
        dmg = self.attack_power
        print(f"{self.name} 기본 공격! ({dmg})")
        target.take_damage(dmg)

    # 강력한 공격을 하는 대신 반동 데미지
    def special_attack(self, target):
        # 특수 공격을 하면 2배의 데미지를 줌 
        dmg = self.attack_power * 2
        print(f"{self.name} 특수공격 [강력한 일격]! ({dmg})")
        target.take_damage(dmg)
        # 5의 반동 데미지를 주게 설정
        # 반동 데미지로 인한 현재 체력 출력  
        self.health = max(0, self.health - 5)
        print(f"{self.name} 반동으로 체력 -5 (현재 {self.health})")
