from pathlib import Path

directory = Path(r"C:\Users\zicke\Desktop\netology\Python\Reps\detective")
line_count = []
book_content = {}
sorted_book = {}

for file in directory.glob("*.txt"):
    if not file.is_file() or not file.exists():
        continue

    local_count = 0
    for line in file.read_text(encoding="UTF=8").splitlines():
        line = line.strip()
        if not line:
            continue
        local_count += 1

    book_chapter = {file.name: local_count}
    book_content.update(book_chapter)
    line_count.append(local_count)
    line_count.sort()

sorted_keys = sorted(book_content, key=book_content.get)

for chapter in sorted_keys:
    sorted_book[chapter] = book_content[chapter]


def string_combiner():
    with open(file="detective.txt", mode="w+", encoding="UTF-8") as new_book:
        for chapters, string_numbs in sorted_book.items():
            with open(file=chapters, mode="r", encoding="UTF-8") as temp_book:
                new_book.write(f"{chapters}\n{string_numbs}\n{temp_book.read()}\n")
            temp_book.close()
    new_book.close()


string_combiner()
