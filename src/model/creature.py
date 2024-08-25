# 초기모델이므로 pydantic이 제공하는 필수값과 선택값 또는 제약 사항 기능을 사용하지 않음
# 나중에 로직을 크게 변경하지않고 개선 가능함
from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    # 두 문자로 된 ISO 국가 코드를 사용, 자주 사용하지않는 국가 코드를 조회하는 데 드는 시간과 타이핑수고를 줄인다
    country: str
    area: str
    description: str
    aka: str