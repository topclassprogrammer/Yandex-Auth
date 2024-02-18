import unittest

import pytest
from selenium.common import NoSuchElementException

from main import click_on, input_in


class TestInput(unittest.TestCase):
    def test_input_in(self):
        target_input = ('input', 'id', 'passp-field-login', 'ivan')
        result = input_in(*target_input)
        expected = True
        self.assertEqual(result, expected)


class TestClick(unittest.TestCase):
    def test_click_for_exception(self):
        target_click = ('test_tag', 'test_attr', 'test_attr_value')
        with self.assertRaises(NoSuchElementException):
            click_on(*target_click)


@pytest.mark.parametrize(
    ('tag', 'attr', 'attr_value', 'expected'), [(
     'button', 'data-type', 'login', True),
     ('button', 'id', 'passp:sign-in', True),
     ('a', 'id', 'passp:exp-register', True),
     ('button', 'data-type', 'phone', True)
    ]
)
def test_click_on(tag, attr, attr_value, expected):
    assert click_on(tag, attr, attr_value) == expected
