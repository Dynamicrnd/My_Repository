# Task 1

english_russian_numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',

}


def num_trunslate (english_number):
    return english_russian_numbers.get(english_number)

print(num_trunslate('seven'))