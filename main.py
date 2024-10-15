# bookbot function that is reading the text file frankenstein.txt and returning the file as book_texts variable
def bookbot():
    read = "books/frankenstein.txt"
    with open(read) as r:
        book_texts = r.read()
    return book_texts

# word count function to count all the words in the text file with split
def count_words(text):
    words = text.split()
    return len(words)

# character count function calling for the count of all the characters in the text file to include converting all characters to lowercase to be counted properly
# also using isalpha to only count letters and not numbers
# using char counter to add all alphabetic characters to the char_count dictionary
def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

# print report function accepting read, word_count, and char_count as inputs
def print_report(read, word_count, char_count):
    print(f"--- Begin report of {read} ---")
    print(f"{word_count} words found in the document")
    print()

    # characters by frequency in descending order using sorted
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    # print each character count from the sorted frequency variable
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

# changing bookbot into a variable to be used for counting both words and characters
book_texts = bookbot()
word_count = count_words(book_texts)
character_count = count_characters(book_texts)

# final print of the report
print_report("books/frankenstein.txt", word_count, character_count)