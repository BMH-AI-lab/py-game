# 추상 클래스 import
from abc import ABC, abstractmethod

class Character(ABC):
    # 캐릭터 들의 이름, 레벨, 체력, 공격력 저장
    def __init__(self, name, level=1, health=100, attack_power=10):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    # 추상 클래스
    # 공격에 대한 클래스 
    @abstractmethod
    def attack(self, target): pass

    @abstractmethod
    # 특수 공격에 대한 클래스 
    def special_attack(self, target): pass

    # 데미지를 주었으면 멀마나 데미지를 주었는지와 만은 체력 출력 
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name}이(가) {damage} 피해를 입었습니다. (체력 {self.health})")

    # 체력이 0이 아니면 health 리턴함(계속 싸워야 한다는 거임)
    def is_alive(self): return self.health > 0

    # 캐릭터의 현재 스테이터스 
    def show_status(self):
        print(f"[{self.name}] 체력:{self.health}/{self.max_health}, 공격력:{self.attack_power}")

    # 체력을 풀 충전 상채로 초기화 
    def reset_health(self): self.health = self.max_health

    # 이름을 이름을 돌려주는 함수 
    # 캐릭터의 이름이 나오도록 해줌 
    def get_name(self): return self.name
