from battle import Battle
from character import Warrior, Mage, Rogue
from utils import clear_console, reset_resources

# 캐릭터 선택 클래스 
def choose_character(prompt: str):
    # 전사, 마법사, 도적에 대한 튜플 리스트 
    classes = {
        "1": ("전사(Warrior)", Warrior),
        "2": ("마법사(Mage)",  Mage),
        "3": ("도적(Rogue)",   Rogue),
    }

    #  While문으로 올바른 번호를 제대로 입력할 때까지 반복 
    while True:
        print(f"\n{prompt}")
        print("  [1] 전사  | 체력100 공15 특:강력한 일격(2배, 자신-5)")
        print("  [2] 마법사| 체력80  공18 특:파이어볼(1.5배, 마나-20/부족시 예외)")
        print("  [3] 도적  | 체력90  공12 특:급습(70% 성공시 3배)")
        print()

        # 번호 1(전사), 2(마법사), 3(도적)중에 입력해서 직업 정하기  
        sel = input("번호를 입력: ").strip()
        # 만약 직업을 정했으면 캐릭터 이름 쓰기 
        # strip(): 앞뒤 공백 제거
        if sel in classes:
            name = input("캐릭터 이름: ").strip() or classes[sel][0]
            return classes[sel][1](name)
        print("올바른 번호를 입력하세요.")

# 체력과 마나를 초기화 
def reset_resources(ch):
    ch.reset_health()
    if hasattr(ch, "max_mana"):
        ch.mana = ch.max_mana

def main():
    print()
    print("=== RPG 게임 ===")
    # 내가 선택한 캐릭터를 플레이어로 설정 
    player = choose_character("당신의 캐릭터를 선택하세요.")
    while True:
    # 상대 캐릭터를 적으로 설정 
        enemy = choose_character("상대 캐릭터를 선택하세요.")
        reset_resources(player)
        reset_resources(enemy)
        
        # 7초동안 배틀  
        battle = Battle(player, enemy, delay=0.7)
        # 배틀 시작
        player_won = battle.start_battle()

        # 졌을 경우 
        if not player_won:
            print("패배했습니다. 게임을 종료합니다.")
            break

        # 승리 시 계속 여부 "Y"/N 대문자를 써도 소문자로 변환
        # Y를 쓰면 계속 하게 되고, N를 쓰면 게임 종료 
        while True:
            cont = input("새로운 적과 계속 싸우시겠습니까? (y/n): ").strip().lower()
            if cont in ("y", "n"): break
            print("y 또는 n으로 입력해주세요.")    
        if cont == "n":
            print("수고하셨습니다! 게임을 종료합니다.")
            break

if __name__ == "__main__":
    main()
