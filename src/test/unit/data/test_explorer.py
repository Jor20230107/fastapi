import os
import pytest
from src.model.explorer import Explorer
from error import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

from src.data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="JohnDoe", country="JP", description="Tokyo on weekend")

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample    

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("DoeJohn")

def test_modify(sample):
    sample.country = "Korea"
    resp = explorer.modify(sample)
    assert resp == sample

def test_modify_missing():
    thing: Explorer = Explorer(name="Doej", country="ko", description="noman")

    with pytest.raises(Missing):
        _ = explorer.modify(thing)

def test_delete(sample):
    resp = explorer.delete(sample)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample)