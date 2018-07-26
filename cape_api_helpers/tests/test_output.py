import pytest
from cape_api_helpers.output import list_response, true_false_both_filter


def test_list_defaults():
    
    @list_response
    def list_user(request, number_of_items=30, offset=0):
        assert number_of_items == 30
        assert offset == 0

    request = {'args': {}}
    list_user(request)


def test_list_arguments():

    @list_response
    def list_user(request, number_of_items=30, offset=0):
        assert number_of_items == 10
        assert offset == 5

    request = {'args': {'numberofitems' : '10', 'offset' : '5'}}
    list_user(request)


def test_filter():
    request = {'args' : {'read' : 'true'}}
    items = [
        {
            'title' : 'Test 1',
            'read' : True
        },
        {
            'title' : 'Test 2',
            'read' : False
        },
        {
            'title' : 'Test 3',
            'read' : False
        }
    ]

    filtered_items = true_false_both_filter(request, items, 'read')
    assert len(filtered_items) == 1
    
    request = {'args' : {'read' : 'false'}}
    filtered_items = true_false_both_filter(request, items, 'read')
    assert len(filtered_items) == 2

    request = {'args' : {'read' : 'both'}}
    filtered_items = true_false_both_filter(request, items, 'read')
    assert len(filtered_items) == 3
