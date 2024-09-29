import pytest
from unittest import mock
from src.model.creature import Creature
from src.service import creature as code

@pytest.fixture
def sample() -> Creature:
    return Creature(
    name="Yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
)

def test_create(sample):
    with mock.patch("src.data.creature.create", return_value=sample):
        resp = code.create(sample)
        assert resp == sample

def test_get_exists():
    with mock.patch("src.data.creature.get_one", return_value="Yeti"):
        resp = code.get_one("Yeti")
        assert resp == "Yeti"

def test_get_missing():
    with mock.patch("src.data.creature.get_one", return_value=None):
        resp = code.get_one("boxturtle")
        assert resp is None