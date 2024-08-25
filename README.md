# fastapi
fastapi_tutorial

## 파일 및 디렉터리 구조
- src : 모든 웹사이트의 코드를 포함한다
- web : FastAPI 웹 계층
- service : 비즈니스 로직 계층
- data : 저장소와의 인터페이스 계층
- model : Pydantic 모델 정의
- fake : 미리 하드코딩된(stub) 데이터

- __init__.py 디렉터리를 패키지로 취급
- creature.py 현재 계층에서 다루는 크리처에 대한 코드
- explorer.py 현재 계층에서 다루는 탐험가에 대한 코드