import sys

from stats import word_count, character_count, sort_character_count


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    wc = word_count(contents)
    cc = character_count(contents)
    sorted_cc = sort_character_count(cc)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for char_count in sorted_cc:
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
