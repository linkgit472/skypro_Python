import pytest
from string_utils import StringUtils

string = StringUtils()


@pytest.mark.parametrize("input, output", [
    ('skypro', 'Skypro'),
    ('hello', 'Hello'),
    ('hello world!', 'Hello world!'),
    ('skyPRO', 'SkyPRO')])
def test_capitalize_positive(input, output):
    assert string.capitalize(input) == output


@pytest.mark.parametrize("input, output", [
    ('', ''),
    ('   ', '   '),
    ('August 27', 'August 27'),
    ('27 august', '27 august')])
def test_capitalize_negative(input, output):
    assert string.capitalize(input) == output


def test_capitalize_negative_none():
    with pytest.raises(AttributeError):
        string.capitalize(None)


@pytest.mark.parametrize("input, output", [
    (' hello', 'hello'),
    ('   Skypro', 'Skypro'),
    (' skypro ', 'skypro '),
    (' hello world', 'hello world')])
def test_trim_positive(input, output):
    assert string.trim(input) == output


@pytest.mark.parametrize("input, output", [
    ('', ''),
    ('   ', ''),
    ('Hello world', 'Hello world'),
    ('hello ', 'hello ')])
def test_trim_negative(input, output):
    assert string.trim(input) == output


@pytest.mark.parametrize("input, sym, output", [
    ('skypro', 'y', True),
    ('hello world', 'o', True),
    (' hello', ' ', True),
    ('skypro', 'sky', True)
    ])
def test_contains_positive(input, sym, output):
    assert string.contains(input, sym) == output


@pytest.mark.parametrize("input, sym, output", [
    ('', '', True),
    ('skypro', 'S', False),
    ('SkyPro', '', True),
    ('', 'a', False),
    ('skypro', 'a', False),
    ])
def test_contains_negative(input, sym, output):
    assert string.contains(input, sym) == output


@pytest.mark.parametrize("input, sym, output", [
        ('skypro', 'y', 'skpro'),
        ('hello world', 'o', 'hell wrld'),
        (' hello', ' ', 'hello'),
        ('skypro', 'sky', 'pro')
        ])
def test_delete_symbol_positive(input, sym, output):
    assert string.delete_symbol(input, sym) == output


@pytest.mark.parametrize("input, sym, output", [
    ('skypro', 'a', 'skypro'),
    ('skypro', 'S', 'skypro'),
    ('hello world', '', 'hello world'),
    ('', 'a', '')
    ])
def test_delete_symbol_negative(input, sym, output):
    assert string.delete_symbol(input, sym) == output
