from string import punctuation as punctuation_chars

import enchant

enchant.set_param("enchant.myspell.dictionary.path", "dict")

# Create dictionary instance.
d = enchant.Dict("ru_RU")

# Russian text to check.
text_to_check = "Пришло теплое лето. На лисной опушки распускаюца колоколчики, незабутки, шыповник. Белые ромашки " \
                "пратягивают к сонцу свои нежные лепески. Вылитают из уютных гнёзд птинцы. У зверей взраслеет смена. " \
                "Мидвежата старше всех."


def find_misspelled_words(text):
    """
    Find all misspelled words in a given text.
    Strip out punctuation chars.
    Lowercase found misspelled words.
    :param text: text to check (str)
    :return: found misspelled words (list)
    """
    return [w.strip(punctuation_chars).lower() for w in text.split() if not d.check(w.strip(punctuation_chars))]


def main():
    """
    Check provided Russian demo text, print the result.
    :return: None
    """
    print(find_misspelled_words(text_to_check))


if __name__ == "__main__":
    main()
