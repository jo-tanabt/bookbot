def count_words(book):
    words = book.split()
    return len(words)

def count_char(book):
    book_lower = book.lower()
    results = {}
    for char in set(book_lower):
        if char.isalpha():
            char_count = book_lower.count(char)
            results[char] = char_count
    return results

with open("books/frankenstein.txt") as f:
    file_content = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_content)} words were found in the document")
    for char, count in count_char(file_content).items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")