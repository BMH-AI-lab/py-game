import random, time
from character.character import Character 

# 한 번의 1 대 1 전투를 관리하는 클래스
class Battle:
    # 전투에 참여할 두 캐릭터를 저장
    # 출력 사이 텀을 주는 delay 값을 보관(음수 방지)
    def __init__(self, fighter1: Character, fighter2: Character, delay: float = 0.7):
        self.f1, self.f2 = fighter1, fighter2
        self.delay = delay

    def _take_turn(self, attacker: Character, defender: Character):
        time.sleep(self.delay)
        # 한 캐릭터의 턴을 처리
        # 70% 기본공격 / 30% 특수공격으로 설정 
        action = "basic" if random.random() < 0.7 else "special"
        try:
            # 선택된 행동을 실행
            # 기본 공격이면 attack, 특수 공격이면 special_attack 호출
            if action == "basic":
                attacker.attack(defender)
            else:
                attacker.special_attack(defender)  # 마나 부족 시 예외 발생 가능
        # 예측 가능한 게임 내 실패만 잡아 출력. 
        # 예를 들어 마법사의 마나 부족을 ValueError로 던지게 함 
        except Exception as e:
            print(f"공격 실패: {e}")  # 예외 처리 (공격 불가, 턴 소모)
        # 턴 종료 전 잠깐 대기.
        time.sleep(self.delay)

    def start_battle(self) -> bool:
        """전투 실행, f1(플레이어) 승리 True/패배 False 반환"""
        print("=== 전투 시작 ===")
        self.f1.show_status()
        self.f2.show_status()

        # 선공 랜덤으로 설정 
        # 공격자 상대 설정 
        turn = self.f1 if random.random() < 0.5 else self.f2
        other = self.f2 if turn is self.f1 else self.f1
        print(f"선공: {turn.get_name()}")

        # 턴 기반 전투
        while self.f1.is_alive() and self.f2.is_alive():
            # 라운드 번호를 출력하고 공격자 턴을 실행
            print(f"\n{turn.get_name()}의 턴")
            self._take_turn(turn, other)
            # 첫 타에 쓰러졌으면 반격 없이 즉시 종료.
            if not other.is_alive(): break
            # 상대가 살아 있으면 곧바로 반격 턴 실행.
            print(f"{other.get_name()}의 반격")
            self._take_turn(other, turn)

            print("\n----- 상태 -----")
            self.f1.show_status()
            self.f2.show_status()
        # 라운드 말 상태를 보여주고 라운드 증가
        winner = self.f1 if self.f1.is_alive() else self.f2
        print("\n=== 전투 종료 ===")
        print(f"승자: {winner.get_name()}")
        # 루프가 끝나면 생존해 있는 쪽이 승자
        # 플레이어가 이겼는지 여부를 True 또는 False로 반환
        # 바깥의 게임 루프에서 승리 시 계속할지 물어보고, 패배 시 종료
        return self.f1.is_alive()