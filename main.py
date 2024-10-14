def bookbot():
    read = "books/frankenstein.txt"
    with open(read) as r:
        book_texts = r.read()
    return book_texts

#bookbot()

def count_words(text):
    words = text.split()
    return len(words)

book_texts = bookbot()
word_count = count_words(book_texts)

print(f"Word count: {word_count}")