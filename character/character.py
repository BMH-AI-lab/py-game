from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, level=1, health=100, attack_power=10):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    # 추상 클래스
    @abstractmethod
    def attack(self, target): pass

    @abstractmethod
    def special_attack(self, target): pass

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name}이(가) {damage} 피해를 입었습니다. (체력 {self.health})")

    def is_alive(self): return self.health > 0

    def show_status(self):
        print(f"[{self.name}] 체력:{self.health}/{self.max_health}, 공격력:{self.attack_power}")

    def reset_health(self): self.health = self.max_health

    def get_name(self): return self.name
