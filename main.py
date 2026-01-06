path = "books/frankenstein.txt"
def get_book_text(book):
    with open(book) as f:
        temp_file = f.read()
    return temp_file
def word_count(book):
    text = get_book_text(book)
    individual_words = text.split()
    number = len(individual_words)
    return number
def main():
    number_of_words = word_count(path)
    result = f"Found {number_of_words} total words"
    print(result)
main()
