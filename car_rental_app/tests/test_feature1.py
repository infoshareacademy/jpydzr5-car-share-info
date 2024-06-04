from feature1 import get_rental_location
from pytest import MonkeyPatch
from copy import deepcopy


# Enter valid input to see if test is passed
def test_get_rental_location_valid1(monkeypatch: MonkeyPatch):
    inputs = ["", "00-000", ""]

    # Deepcopy tuple for tests result
    inputs_ = tuple(deepcopy(inputs))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    result = get_rental_location()
    assert result == inputs_


# Enter invalid input to see if test is passed
def test_get_rental_location_invalid1(monkeypatch: MonkeyPatch):
    inputs = ["", "", ""]

    # Deepcopy tuple for tests result
    inputs_ = tuple(deepcopy(inputs))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    result = get_rental_location()
    # ValueError returns None
    assert result is None
