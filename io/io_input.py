import re


def reverse(text):
    return text[::-1]


def remove_punctuation(text):
    return re.sub(r'[?!.\"\'\[\]();:\-\\,]', '', text)


def remove_space(text):
    return text.replace(" ", "")


def low_case(text):
    return text.lower()


def processing_text(text):
    processed_text = low_case(remove_space(remove_punctuation(text)))
    print(processed_text)
    return processed_text


def is_palindrome(text):
    return processing_text(text) == processing_text(reverse(text))


# something = input('Enter text: ')

# if is_palindrome(something):
#     print('Yes, it is a palindrome')
#
# else:
#     print('No, it is not a palindrome')

assert is_palindrome("Rise to Vote, Sir") is True
assert is_palindrome("Ris..e to Vote, Sir") is True
assert is_palindrome("A nut for a jar of tuna.") is True



