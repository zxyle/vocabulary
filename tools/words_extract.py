import re
from spellchecker import SpellChecker

spell = SpellChecker()


with open("book.txt", encoding="utf-8") as f, \
        open("words.txt", "w", encoding="utf-8") as f2:
    text = f.read()
    text = text.lower()
    pattern = re.compile(r"[a-zA-Z]{4,17}")
    words = pattern.findall(text)

    words = list(set(words))
    words.sort()
    misspelled = spell.unknown(words)

    for word in misspelled:
        print(word)
        words.remove(word)

    f2.write("\n".join(words))
