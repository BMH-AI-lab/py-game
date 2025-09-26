# 리스트의 이름들을 패키지화 외부 코드에서 쓸 수 있게 함
#  "공식 인터페이스"를 정리해주는 역할을 하게 함 

from .battle_manage import Battle

__all__ = ["Battle"]
