import pytest
from unittest import mock
from src.model.explorer import Explorer
from src.service import explorer as code

@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="JohnDoe",
        country="JP",
        description="nigiri"
    )

def test_create(sample):
    with mock.patch("src.data.explorer.create", return_value=sample):
        resp = code.create(sample)
        assert resp == sample

def test_get_exists():
    with mock.patch("src.data.explorer.get_one", return_value="Yeti"):
        resp = code.get_one("Yeti")
        assert resp == "Yeti"
    
def test_get_missing():
    with mock.patch("src.data.explorer.get_one", return_value=None):
        resp = code.get_one("boxturtle")
        assert resp is None