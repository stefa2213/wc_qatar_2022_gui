import pytest
import library


def test_fahrenheit_to_celsius():
    f = 32
    c = library.fahrenheit_to_celsius(f)
    assert c == 0


def test_cels_to_fharenheit():
    c = 0
    f = library.celsius_to_fahrenheit(c)
    assert f == 32

# run in terminal:
# coverage run --source="." --omit="*/venv/*" -m pytest
# coverage report library.py
