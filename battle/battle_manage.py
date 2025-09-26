# battle/battle_manage.py
import random, time
from character.character import Character 

class Battle:
    def __init__(self, fighter1: Character, fighter2: Character, delay: float = 0.7):
        self.f1, self.f2 = fighter1, fighter2
        self.delay = delay

    def _take_turn(self, attacker: Character, defender: Character):
        time.sleep(self.delay)
        # 70% 기본공격 / 30% 특수공격
        action = "basic" if random.random() < 0.7 else "special"
        try:
            if action == "basic":
                attacker.attack(defender)
            else:
                attacker.special_attack(defender)  # 마나 부족 시 예외 발생 가능
        except Exception as e:
            print(f"공격 실패: {e}")  # 예외 처리 (공격 불가, 턴 소모)
        time.sleep(self.delay)

    def start_battle(self) -> bool:
        """전투 실행, f1(플레이어) 승리 True/패배 False 반환"""
        print("=== 전투 시작 ===")
        self.f1.show_status()
        self.f2.show_status()

        # 선공 랜덤
        turn = self.f1 if random.random() < 0.5 else self.f2
        other = self.f2 if turn is self.f1 else self.f1
        print(f"선공: {turn.get_name()}")

        # 턴 기반 전투
        while self.f1.is_alive() and self.f2.is_alive():
            print(f"\n{turn.get_name()}의 턴")
            self._take_turn(turn, other)
            if not other.is_alive(): break

            print(f"{other.get_name()}의 반격")
            self._take_turn(other, turn)

            print("\n----- 상태 -----")
            self.f1.show_status()
            self.f2.show_status()

        winner = self.f1 if self.f1.is_alive() else self.f2
        print("\n=== 전투 종료 ===")
        print(f"승자: {winner.get_name()}")
        return self.f1.is_alive()