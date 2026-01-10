import sys
if len(sys.argv) < 2:
    raise Exception("Usage: python3 main.py <path_to_book>")
else:
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    def get_book_text(book):
        with open(book) as f:
            temp_file = f.read()
        return temp_file
    from stats import get_num_words
    from stats import letter_count
    from stats import sorted_count_on
    from stats import sorted_count
    def main():
        text = get_book_text(path)
        number_of_words = get_num_words(text)
        result = f"Found {number_of_words} total words"
        print(result)
        print("-------- Character Count --------")
        character_count = letter_count(text)
        sorted_chars = sorted_count(character_count)
        sorted_letters = []
        for item in sorted_chars:
            ch = item["char"]
            count = item["num"]
            if ch.isalpha():
                print(f"{ch}: {count}")
    main()
