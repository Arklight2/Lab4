def count_longest_word(Task2):
    chars_to_remove = ".,!?:;\"'-"
    with open(Task2, 'r', encoding='utf-8') as file:
        text = file.read()
    translation_table = str.maketrans('', '', chars_to_remove)
    cleaned_text = text.translate(translation_table)
    words = cleaned_text.split()
    longest_word = max(words, key=len)
    count = words.count(longest_word)
    return longest_word, count

Task2 = "C:/Users/balbe/Downloads/task2F.txt"
longest_word, count = count_longest_word(Task2)

print(f"Самое длинное слово: '{longest_word}'")
print(f"Оно встречается {count} раз(а).")