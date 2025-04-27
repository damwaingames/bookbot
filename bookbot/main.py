import typer
from typing_extensions import Annotated

from stats import word_count, character_count, sort_character_count

app = typer.Typer(help="BookBot generate statistical report of text documents.")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


@app.command()
def report(
    path: Annotated[
        str, typer.Argument(help="Path to file containing text to analyse.")
    ],
) -> None:
    """
    Generate a report on file at PATH.
    """
    contents = get_book_text(path)
    wc = word_count(contents)
    cc = character_count(contents)
    sorted_cc = sort_character_count(cc)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for char_count in sorted_cc:
        print(f"{char_count['char']}: {char_count['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    app()
