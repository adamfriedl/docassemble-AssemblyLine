import pytest


@pytest.fixture
def broken():
    raise RuntimeError("fixture setup failed")


def test_uses_broken_fixture(broken):
    assert True
