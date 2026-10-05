import logging
import unittest

import pytest


def test_plain_failure():
    logging.getLogger().error("this log line should not be annotated")
    assert 1 + 1 == 3


@pytest.mark.parametrize("value", ["has space", "ok"])
def test_parametrized(value):
    assert value == "ok"


class TestInClass(unittest.TestCase):
    def test_method(self):
        self.assertEqual("a", "b")


def test_passes():
    assert True
