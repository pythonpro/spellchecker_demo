import pytest

from spellchecker import find_misspelled_words


def test_russian_positive_result():
    text = 'Мошина ехала по соссе.'
    assert find_misspelled_words(text) == ['мошина', 'соссе']


def test_russian_negative_result():
    text = 'Машина ехала по шоссе.'
    assert find_misspelled_words(text) == []


@pytest.mark.skip(reason='English is not supported yet')
def test_english_positive_result():
    text = "Hallo, wold! I'm a doctor."
    assert find_misspelled_words(text) == ['hallo', 'wold']
