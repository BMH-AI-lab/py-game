import os
import random

def clear_console():
    """콘솔 화면 지우기 (운영체제별 지원)"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_choice(prompt: str, choices: dict):
    """
    사용자 입력을 받아 choices 중 하나를 반환.
    choices 예시: {"1": "전사", "2": "마법사"}
    """
    while True:
        print(prompt)
        for key, val in choices.items():
            print(f" [{key}] {val}")
        sel = input("번호를 입력하세요: ").strip()
        if sel in choices:
            return sel
        print("올바른 번호를 입력하세요.")


def reset_resources(character):
    """체력과 마나를 초기화"""
    character.reset_health()
    if hasattr(character, "max_mana"):
        character.mana = character.max_mana


def weighted_choice(options: list, weights: list):
    """
    확률 기반 선택 (예: 기본공격 70%, 특수공격 30%)
    options: ["basic", "special"]
    weights: [0.7, 0.3]
    """
    return random.choices(options, weights=weights, k=1)[0]
