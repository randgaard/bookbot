def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        word_count = count_words(file_contents)

        char_count = count_characters(file_contents)

        sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f'Number of words in the document: {word_count}\n')
        
        for char, count in sorted_char_count:
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    character_count = {}

    for char in text:
        if char.isalpha():
            character_count[char] = character_count.get(char, 0) + 1

    return character_count

main()