def is_isogram(word):
    word = word.lower()
    unique_chars = set(word)
    return len(word) == len(unique_chars)

print(is_isogram("isogram"))
print(is_isogram("sets"))
print(is_isogram("Tea"))