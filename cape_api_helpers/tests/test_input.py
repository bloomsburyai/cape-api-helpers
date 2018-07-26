import pytest
from cape_api_helpers.input import required_parameter, optional_parameter
from cape_api_helpers.exceptions import UserException


def test_required_parameter():
    request = {'args': {'test' : 'testing'}}
    test = required_parameter(request, 'test')
    assert test == 'testing'


def test_case_insensitive():
    request = {'args': {'test' : 'testing'}}
    test = required_parameter(request, 'TEST')
    assert test == 'testing'
    

def test_missing_required_parameter():
    with pytest.raises(UserException):
        request = {'args': {'test' : 'testing'}}
        test = required_parameter(request, 'missing')


def test_optional_parameter():
    request = {'args': {'test': 'testing'}}
    test = optional_parameter(request, 'test', 'hello')
    assert test == 'testing'


def test_missing_optional_parameter():
    request = {'args': {'test': 'testing'}}
    test = optional_parameter(request, 'missing', 'hello')
    assert test == 'hello'
