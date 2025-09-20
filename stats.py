def get_book_text(book_path):
    with open(book_path) as f:
        file_content = f.read()
        num_words = len(file_content.split(maxsplit=-1))
        print(f"Found {num_words} total words")


def get_character_count(book_path):
    char_count = {}
    with open(book_path) as f:
        file_content = f.read()
        file_content = file_content.lower()
        num_characters = file_content
        for char in num_characters:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def character_sort(char_count):
    alpha_only_counts = {char: count for char, count in char_count.items() if char.isalpha()}
    sorted_char_count = dict(sorted(alpha_only_counts.items(), key=lambda item: item[1], reverse=True))
    for char, count in sorted_char_count.items():
        print(f"{char}: {count}")