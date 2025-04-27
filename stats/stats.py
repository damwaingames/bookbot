def word_count(contents: str) -> int:
    return len(contents.split())


def character_count(contents: str) -> dict[str, int]:
    results: dict[str, int] = {}
    for char in contents.lower():
        if char in results.keys():
            results[char] += 1
        else:
            results[char] = 1
    return results


def sort_character_count(characters: dict[str, int]) -> list[dict[str, int | str]]:
    character_counts: list[dict[str, int | str]] = []
    for char, count in characters.items():
        if char.isalpha():
            character_counts.append({"char": char, "num": count})
    character_counts.sort(key=lambda item: item["num"], reverse=True)
    return character_counts
