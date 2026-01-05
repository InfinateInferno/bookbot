path = "books/frankenstein.txt"
def get_book_text(book):
    with open(book) as f:
        temp_file = f.read()
    return temp_file
def main():
    text = get_book_text(path)
    print(text)
main()
