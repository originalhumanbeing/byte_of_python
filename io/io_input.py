def reverse(text):
    return text[::-1]

def remove_punctuation(text):
    if '.' in text:
        result = text.replace(".", "")
    if '?' in text:
        result = text.replace("?", "")
    if "!" in text:
        result = text.replace("!", "")
    if ':' in text:
        result = text.replace(":", "")
    if ';' in text:
        result = text.replace(";", "")
    if '-' in text:
        result = text.replace("-", "")
    if '()' in text:
        result = text.replace("()", "")
    if '[]' in text:
        result = text.replace("[]", "")
    if '...' in text:
        result = text.replace("...", "")
    if '\'' in text:
        result = text.replace("\'", "")
    if '""' in text:
        result = text.replace('""', "")
    if '\\' in text:
        result = text.replace("\\", "")
    if ',' in text:
        result = text.replace(",", "")
    else:
        result = reverse(text)
    return result

def remove_space(text):
    return text.replace(" ", "")

def low_case(text):
    return text.lower()

def processing_text(text):
    return low_case(remove_space(remove_punctuation(text)))

def is_palindrome(text):
    processed_text = processing_text(text)
    return processed_text == low_case(remove_space(remove_punctuation(reverse(text))))

something = input('Enter text: ')

if is_palindrome(something):
    print('Yes, it is a palindrome')

else:
    print('No, it is not a palindrome')

