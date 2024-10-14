import re

def bookbot():
    read = "books/frankenstein.txt"
    with open(read) as file:
        texts = file.read()
    return texts

def extract_story(texts, start_marker, end_marker):
    start_index = texts.find(start_marker)
    end_index = texts.rfind(end_marker)
    return texts[start_index:end_index] if start_index != -1 and end_index != -1 else texts

def word_count(texts):
    counting_words = re.sub(r'[^\w\s]', '', texts)
    words = counting_words.split()
    return len(words)

frankenstein_text = bookbot()

# Use distinctive phrases found in your analysis
start_marker = "Frankenstein, or the Modern Prometheus by Mary Wollstonecraft (Godwin) Shelley"
end_marker = "He sprang from the cabin window as he said this, upon the ice raft which lay close to the vessel.  He was soon borne away by the waves and lost in darkness and distance."

# Extract the story using markers
main_story = extract_story(frankenstein_text, start_marker, end_marker)

# Now count only the main story words
number_of_words = word_count(main_story)

print(f"Number of words in Frankenstein (main story): {number_of_words}")