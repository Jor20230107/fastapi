from fastapi import APIRouter, HTTPException
from src.model.explorer import Explorer
from src.service import explorer as service
from error import Duplicate, Missing

router = APIRouter(prefix="/explorer")

@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)    

# 나머지 엔드포인트. 현재는 아무 일도 하지 않는다.
@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)    

@router.patch("/{name}/")
@router.patch("/{name}")
def modify(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.put("/{name}/")
@router.put("/{name}")
def replace(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.replace(id, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)    

@router.delete("/{name}/", status_code=204)
@router.delete("/{name}", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    